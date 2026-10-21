"""检查课程辅助代码的文件操作、预览、案例生成和响应注入行为。"""
import base64
import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.parse
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEST_TEMP = ROOT / ".runtime/infrastructure-tests"
TEST_TEMP.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(ROOT / "starters"))
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "starters/hw02"))
from shared.diagram_io import DiagramError, apply_operations, read_diagram, workspace_file
from make_cases import document, performance
from make_safety_cases import generate
from replay import ReplayModel

spec = importlib.util.spec_from_file_location("preview", ROOT / "starters/hw01/preview.py")
preview = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preview)


class AdapterTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=TEST_TEMP)
        self.addCleanup(self.tmp.cleanup)
        self.workspace = Path(self.tmp.name)
        self.path = self.workspace / "test.drawio"
        self.path.write_bytes((ROOT / "materials/fixtures/labels.drawio").read_bytes())

    def test_read_and_atomic_batch(self):
        before = read_diagram(self.workspace, "test.drawio")
        ops = [{"op": "rename_node", "page_id": "page-a", "cell_id": "n2", "label": "复核"}, {"op": "add_edge", "page_id": "page-a", "cell_id": "return", "source": "n3", "target": "n2"}]
        after = apply_operations(self.workspace, "test.drawio", before["version"], ops)
        self.assertNotEqual(before["version"], after["version"])
        self.assertIn("复核", self.path.read_text(encoding="utf-8"))
        with self.assertRaisesRegex(DiagramError, "version_conflict"):
            apply_operations(self.workspace, "test.drawio", before["version"], ops)
        changed = self.path.read_bytes()
        invalid_batch = copy.deepcopy(ops)
        invalid_batch[0]["label"] = "should not persist"
        invalid_batch[1]["source"] = "missing"
        with self.assertRaises(DiagramError):
            apply_operations(self.workspace, "test.drawio", after["version"], invalid_batch)
        self.assertEqual(changed, self.path.read_bytes())

    def test_endpoints_and_duplicate_operation(self):
        before = read_diagram(self.workspace, "test.drawio")
        op = {"op": "set_endpoints", "page_id": "page-a", "cell_id": "e1", "source": "n3", "target": "n1"}
        after = apply_operations(self.workspace, "test.drawio", before["version"], [op])
        edge = next(c for c in after["pages"][0]["cells"] if c["id"] == "e1")
        self.assertEqual(edge["source"], "n3")
        original = self.path.read_bytes()
        duplicate = {"op": "add_edge", "page_id": "page-a", "cell_id": "e1", "source": "n1", "target": "n2"}
        with self.assertRaises(DiagramError):
            apply_operations(self.workspace, "test.drawio", after["version"], [duplicate])
        self.assertEqual(original, self.path.read_bytes())

    def test_workspace_rejects_paths(self):
        for name in ("../a.drawio", "sub/a.drawio", "sub\\a.drawio", "C:a.drawio", "a.txt", "x.drawio:stream.drawio", 42):
            with self.subTest(name=name), self.assertRaises(DiagramError):
                workspace_file(self.workspace, name)

    def test_failed_replace_preserves_file_and_removes_temporary(self):
        before = read_diagram(self.workspace, "test.drawio")
        original = self.path.read_bytes()
        op = {"op": "rename_node", "page_id": "page-a", "cell_id": "n2", "label": "changed"}
        with patch("shared.diagram_io.os.replace", side_effect=OSError("synthetic write error")):
            with self.assertRaisesRegex(OSError, "synthetic"):
                apply_operations(self.workspace, "test.drawio", before["version"], [op])
        self.assertEqual(original, self.path.read_bytes())
        self.assertEqual(list(self.workspace.glob("*.tmp")), [])

    def test_dtd_invalid_and_size(self):
        for name in ("external-entity.drawio", "invalid.drawio"):
            self.path.write_bytes((ROOT / "materials/fixtures" / name).read_bytes())
            with self.assertRaises(DiagramError):
                read_diagram(self.workspace, "test.drawio")
        self.path.write_bytes(b" " * (2*1024*1024+1))
        with self.assertRaisesRegex(DiagramError, "2 MiB"):
            read_diagram(self.workspace, "test.drawio")


class MaterialTests(unittest.TestCase):
    def test_preview_safe_text_and_roundtrip(self):
        data = json.loads((ROOT / "materials/cases/preview-example.json").read_text(encoding="utf-8"))
        data["nodes"][0]["label"] = '<script>alert("x")</script> 中文 & 😀'
        with tempfile.TemporaryDirectory(dir=TEST_TEMP) as temp:
            svg, drawio = Path(temp)/"out.svg", Path(temp)/"out.drawio"
            preview.render(data, svg)
            preview.render(data, drawio)
            xml = ET.parse(svg)
            self.assertFalse(any(e.tag.endswith("script") for e in xml.iter()))
            snapshot = read_diagram(Path(temp), "out.drawio")
            self.assertIn(data["nodes"][0]["label"], [c.get("value") for c in snapshot["pages"][0]["cells"]])

    def test_compressed_fixture(self):
        page = ET.parse(ROOT / "materials/fixtures/compressed.drawio").find("diagram")
        inflated = urllib.parse.unquote(zlib.decompress(base64.b64decode(page.text), -15).decode("utf-8"))
        normal = ET.parse(ROOT / "materials/fixtures/normal.drawio").find("diagram/mxGraphModel")
        self.assertEqual(ET.tostring(ET.fromstring(inflated)), ET.tostring(normal))

    def test_fixture_page_identity(self):
        root = ET.parse(ROOT / "materials/fixtures/multi-page.drawio")
        pages = root.findall("diagram")
        self.assertEqual([p.get("id") for p in pages], ["page-a", "page-b"])
        self.assertEqual(pages[0].find(".//mxCell[@id='n2']").get("value"), "Step 2")
        self.assertEqual(pages[1].find(".//mxCell[@id='n2']").get("value"), "   ")

    def test_performance_inputs_within_limits(self):
        with tempfile.TemporaryDirectory(dir=TEST_TEMP) as temp:
            performance(Path(temp))
            for name, count in (("small", 21), ("medium", 1001), ("large", 9801)):
                path = Path(temp) / f"{name}.drawio"
                self.assertEqual(len(ET.parse(path).findall(".//mxCell")), count)
                self.assertLess(path.stat().st_size, 2*1024*1024)

    def test_boundary_generator(self):
        with tempfile.TemporaryDirectory(dir=TEST_TEMP) as temp:
            generate(Path(temp))
            for count in (10000, 10001):
                self.assertEqual(len(ET.parse(Path(temp)/f"cells-{count}.drawio").findall(".//mxCell")), count)
            for count in (20, 21):
                self.assertEqual(len(ET.parse(Path(temp)/f"pages-{count}.drawio").findall("diagram")), count)
            for size in (2097152, 2097153):
                self.assertEqual((Path(temp)/f"bytes-{size}.drawio").stat().st_size, size)
            page = ET.parse(Path(temp)/"expanded-over-limit.drawio").find("diagram")
            expanded = urllib.parse.unquote(zlib.decompress(base64.b64decode(page.text), -15).decode("utf-8"))
            self.assertGreater(len(expanded.encode("utf-8")), 8*1024*1024)

    def test_performance_inputs_can_exercise_result_lists(self):
        with tempfile.TemporaryDirectory(dir=TEST_TEMP) as temp:
            performance(Path(temp), with_issues=True)
            for name, nodes in (("small", 10), ("medium", 500), ("large", 4900)):
                root = ET.parse(Path(temp) / f"{name}.drawio")
                steps = root.findall(".//mxCell[@vertex='1']")
                self.assertEqual(len(steps), nodes)
                self.assertEqual(sum(not cell.get("value", "").strip() for cell in steps), nodes // 5)


class ReplayTests(unittest.TestCase):
    def test_multiple_tool_response_preserved(self):
        case = json.loads((ROOT / "materials/cases/replay/multiple-tools.json").read_text(encoding="utf-8"))
        model = ReplayModel(case["messages"])
        first = model([], [])
        self.assertEqual(len(first["tool_calls"]), 2)
        self.assertEqual(first["tool_calls"][1]["function"]["name"], "inspect_diagram")
        self.assertIn("content", model([], []))

    def test_exhaustion_visible(self):
        with self.assertRaisesRegex(RuntimeError, "replay_exhausted"):
            ReplayModel([])([], [])

    def test_model_failure_injected(self):
        with self.assertRaisesRegex(ConnectionError, "synthetic"):
            ReplayModel([{"raise": "synthetic service failure"}])([], [])


if __name__ == "__main__":
    unittest.main()
