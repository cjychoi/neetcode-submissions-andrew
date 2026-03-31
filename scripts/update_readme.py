from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

LANGUAGE_BY_EXT = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".cpp": "C++",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
    ".kt": "Kotlin",
    ".swift": "Swift",
    ".sql": "SQL",
}

START_MARKER = "<!-- START:SOLUTIONS_TABLE -->"
END_MARKER = "<!-- END:SOLUTIONS_TABLE -->"


def is_submission_file(path: Path) -> bool:
    return path.is_file() and path.stem.startswith("submission-")


def get_solution_rows():
    rows = []

    for topic_dir in sorted(ROOT.iterdir(), key=lambda p: p.name.lower()):
        if not topic_dir.is_dir():
            continue

        # Skip hidden/system folders and utility folders
        if topic_dir.name.startswith(".") or topic_dir.name in {"scripts"}:
            continue

        for problem_dir in sorted(topic_dir.iterdir(), key=lambda p: p.name.lower()):
            if not problem_dir.is_dir():
                continue

            submission_files = sorted(
                [f for f in problem_dir.iterdir() if is_submission_file(f)],
                key=lambda p: p.name.lower()
            )

            if not submission_files:
                continue

            exts = sorted({f.suffix for f in submission_files})
            languages = [LANGUAGE_BY_EXT.get(ext, ext.lstrip(".")) for ext in exts]

            rows.append({
                "topic": topic_dir.name,
                "problem": problem_dir.name,
                "languages": ", ".join(languages),
                "submissions": len(submission_files),
                "path": f"`{topic_dir.name}/{problem_dir.name}/`",
            })

    return rows


def build_table(rows):
    if not rows:
        return "_No solutions found yet._"

    lines = [
        "| Topic | Problem | Language | Submissions | Path |",
        "|---|---|---|---:|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row['topic']} | {row['problem']} | {row['languages']} | {row['submissions']} | {row['path']} |"
        )

    total_problems = len(rows)
    total_submissions = sum(r["submissions"] for r in rows)

    summary = [
        f"**Total problems solved:** {total_problems}",
        f"**Total submissions:** {total_submissions}",
        "",
    ]

    return "\n".join(summary + lines)


def update_readme():
    if not README.exists():
        raise FileNotFoundError("README.md not found")

    content = README.read_text(encoding="utf-8")
    table = build_table(get_solution_rows())

    pattern = re.compile(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        re.DOTALL,
    )

    replacement = f"{START_MARKER}\n{table}\n{END_MARKER}"

    if not pattern.search(content):
        raise ValueError(
            "Could not find README markers. Add these lines:\n"
            "<!-- START:SOLUTIONS_TABLE -->\n"
            "<!-- END:SOLUTIONS_TABLE -->"
        )

    new_content = pattern.sub(replacement, content)

    if new_content != content:
        README.write_text(new_content, encoding="utf-8")
        print("README.md updated.")
    else:
        print("README.md already up to date.")


if __name__ == "__main__":
    update_readme()