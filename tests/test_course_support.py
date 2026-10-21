"""检查 MCP 工具结果、个人 fork 模式与文档结构校验。"""
import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "starters"))
sys.path.insert(0, str(ROOT / "tools"))
from shared.tool_result import require_success
import verify_course


class McpResultTests(unittest.TestCase):
    def test_protocol_success_with_tool_failure_is_rejected(self):
        result = SimpleNamespace(isError=False, structuredContent={"ok": False, "data": None, "error": {"code": "missing_file"}})
        with self.assertRaisesRegex(RuntimeError, "未返回成功结果"):
            require_success(result)

    def test_protocol_error_is_rejected(self):
        with self.assertRaisesRegex(RuntimeError, "工具执行错误"):
            require_success(SimpleNamespace(isError=True))

    def test_text_encoded_envelope_is_accepted(self):
        payload = {"ok": True, "data": {"pages": []}, "error": None}
        result = SimpleNamespace(isError=False, structuredContent=None, content=[SimpleNamespace(type="text", text=json.dumps(payload))])
        self.assertEqual(require_success(result), payload)

    def test_malformed_success_is_rejected(self):
        result = SimpleNamespace(isError=False, structuredContent={"ok": True, "data": None, "error": None})
        with self.assertRaisesRegex(RuntimeError, "成功结果应为"):
            require_success(result)


class StudentForkTests(unittest.TestCase):
    def test_completed_starters_allowed_only_in_student_mode(self):
        # 模拟学生完成起始任务，不修改当前工作目录中的文件。
        original_read = Path.read_text
        starters = {ROOT / p for p in ("starters/hw01/prompt_lab.py", "starters/hw02/agent.py", "starters/hw02/tools.py")}

        def completed_read(path, *args, **kwargs):
            content = original_read(path, *args, **kwargs)
            return content.replace("NotImplementedError", "RuntimeError") if path in starters else content

        with patch.object(Path, "read_text", completed_read):
            strict = verify_course.verify()
            student = verify_course.verify(student_work=True)
        starter_errors = [e for e in strict["errors"] if "起始代码未保留" in e]
        self.assertEqual(len(starter_errors), 3)
        self.assertTrue(student["ok"], student["errors"])


class DocumentStructureTests(unittest.TestCase):
    def verify_assignment_text(self, text):
        original_read = Path.read_text
        target = ROOT / "assignments/HW1.md"

        def replacement(path, *args, **kwargs):
            return text if path == target else original_read(path, *args, **kwargs)

        with patch.object(Path, "read_text", replacement):
            return verify_course.verify()

    def test_headings_do_not_require_fixed_wording(self):
        result = self.verify_assignment_text("# 图表实验\n\n本实验比较模型输出。\n\n## 实验说明\n\n请分析输入并记录结果。\n")
        self.assertTrue(result["ok"], result["errors"])

    def test_title_without_body_is_rejected(self):
        result = self.verify_assignment_text("# 图表实验\n\n## 实验说明\n")
        self.assertIn(f"文档缺少正文: {Path('assignments/HW1.md')}", result["errors"])

    def test_heading_inside_code_is_not_a_document_title(self):
        result = self.verify_assignment_text("```python\n# 示例注释\nprint('示例')\n```\n")
        self.assertIn(f"文档缺少标题: {Path('assignments/HW1.md')}", result["errors"])


if __name__ == "__main__":
    unittest.main()
