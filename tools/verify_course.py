"""检查课程结构、文档链接、固定源码引用、课件和实验起始代码。"""
from __future__ import annotations
import ast
import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", ".local", ".runtime", ".venv", "node_modules", "__pycache__"}


def heading_ids(text: str) -> set[str]:
    ids, counts = set(), {}
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        if in_fence:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            title = re.sub(r"[^\w\-\s]", "", match[1].lower()).replace(" ", "-")
            number = counts.get(title, 0)
            counts[title] = number + 1
            ids.add(title + (f"-{number}" if number else ""))
    return ids


def verify(student_work: bool = False) -> dict:
    errors = []
    files = []
    for directory, children, names in os.walk(ROOT):
        children[:] = [name for name in children if name not in SKIP]
        files.extend(Path(directory) / name for name in names)
    md = [p for p in files if p.suffix == ".md"]
    required = [ROOT / f"weeks/week{i:02}.md" for i in range(1, 11)] + [ROOT / f"assignments/HW{i}.md" for i in range(1, 9)]
    for path in required:
        if not path.is_file():
            errors.append(f"缺少课程文件: {path.relative_to(ROOT)}")
    for path in md:
        content = path.read_text(encoding="utf-8")
        # 只检查文档有标题和正文，不限定教学章节的具体名称。
        outside_fences = re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", content, flags=re.M | re.S)
        if not re.search(r"^#\s+\S", outside_fences, re.M):
            errors.append(f"文档缺少标题: {path.relative_to(ROOT)}")
        sections = re.split(r"^#{1,6}\s+.+$", outside_fences, flags=re.M)
        if not any(section.strip() for section in sections[1:]):
            errors.append(f"文档缺少正文: {path.relative_to(ROOT)}")
    forbidden = re.compile(r"vr_server_v2|vr-server-cs146-5w|course_project|组会纪要|五周|已调整至|BASELINE_SHA_TO_FILL")
    links = source_links = 0
    baseline = json.loads((ROOT / "docs/baseline.json").read_text(encoding="utf-8-sig"))
    sha = baseline["commit"]
    if not re.fullmatch(r"[0-9a-f]{40}", sha) or baseline["repository"] != "https://github.com/NewPhrexian/next-ai-draw-io_cs146s":
        errors.append("教学源码仓库或固定提交无效")
    for path in md:
        content = path.read_text(encoding="utf-8")
        if forbidden.search(content):
            errors.append(f"文档包含旧项目或改版说明: {path.relative_to(ROOT)}")
        for raw in re.findall(r"\]\(([^)]+)\)", content):
            target = raw.strip().split(' "', 1)[0].strip("<>")
            parsed = urlparse(target)
            if parsed.scheme:
                if "/next-ai-draw-io_cs146s/blob/" in target:
                    source_links += 1
                    if f"/blob/{sha}/" not in target:
                        errors.append(f"源码链接未指向固定教学提交: {path.relative_to(ROOT)}")
                continue
            destination = path if not parsed.path else path.parent / unquote(parsed.path)
            destination = destination.resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                errors.append(f"链接目标不存在或超出课程目录: {path.relative_to(ROOT)} -> {target}")
            elif parsed.fragment and destination.suffix == ".md" and unquote(parsed.fragment) not in heading_ids(destination.read_text(encoding="utf-8")):
                errors.append(f"找不到链接对应的章节: {path.relative_to(ROOT)} -> {target}")
            links += 1
    manifest = json.loads((ROOT / "materials/slides.sha256.json").read_text(encoding="utf-8-sig"))
    if len(manifest) != 15:
        errors.append("课件清单应包含 15 份文件")
    for entry in manifest:
        path = ROOT / "materials/slides" / entry["file"]
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"].lower():
            errors.append(f"课件缺失或内容与校验值不符: {entry['file']}")
    for path in files:
        if path.suffix == ".py":
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        if path.suffix == ".json":
            json.loads(path.read_text(encoding="utf-8-sig"))
        if path.name in {".env", ".env.local", ".gitmodules"} or path.suffix in {".gguf", ".safetensors", ".sqlite", ".zip"}:
            errors.append(f"课程目录中包含不应提交的文件: {path.relative_to(ROOT)}")
    if not student_work:
        for name in ("starters/hw01/prompt_lab.py", "starters/hw02/agent.py", "starters/hw02/tools.py"):
            if "NotImplementedError" not in (ROOT / name).read_text(encoding="utf-8"):
                errors.append(f"起始代码未保留学生实现任务: {name}")
    cases = json.loads((ROOT / "materials/cases/prompt-cases.json").read_text(encoding="utf-8"))
    if len(cases) != 8 or [sum(c["split"] == s for c in cases) for s in ("dev", "eval")] != [4, 4]:
        errors.append("HW1 应包含 4 个开发案例和 4 个评估案例")
    if len(json.loads((ROOT / "materials/cases/agent-cases.json").read_text(encoding="utf-8"))) != 6:
        errors.append("HW2 应包含 6 个模型实验案例")
    for old in ("course_project", "five_week_plan.md"):
        if (ROOT / old).exists():
            errors.append(f"旧课程路径仍然存在: {old}")
    return {"ok": not errors, "files": len(files), "markdown": len(md), "weeks": 10, "assignments": 8, "slides": len(manifest), "local_links": links, "pinned_source_links": source_links, "errors": errors}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="检查课程文件、链接、课件和起始代码的一致性。")
    parser.add_argument("--student-work", action="store_true", help="检查个人 fork，允许学生已经完成起始代码中的任务")
    args = parser.parse_args()
    result = verify(student_work=args.student_work)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["ok"] else 1)
