#!/usr/bin/env python3
import os
import re
from typing import Optional

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find_matching_div_end(html: str, start_pos: int) -> Optional[int]:
    # start_pos is the index just AFTER the opening <div ...>
    open_tag = re.compile(r"<div\b", re.IGNORECASE)
    close_tag = re.compile(r"</div\s*>", re.IGNORECASE)

    depth = 1
    pos = start_pos
    while depth > 0:
        m_open = open_tag.search(html, pos)
        m_close = close_tag.search(html, pos)
        if not m_close and not m_open:
            return None
        if m_open and (not m_close or m_open.start() < m_close.start()):
            depth += 1
            pos = m_open.end()
        else:
            depth -= 1
            pos = m_close.end()
    return pos


def remove_div_by_class(html: str, class_name: str) -> str:
    # Remove ALL div blocks whose class attribute contains exactly class_name
    # Match opening tag for target class
    pattern = re.compile(
        r"<div\s+class=\"" + re.escape(class_name) + r"\"[^>]*>",
        re.IGNORECASE,
    )

    changed = True
    while changed:
        changed = False
        m = pattern.search(html)
        if not m:
            break
        start = m.start()
        end_open = m.end()
        end = find_matching_div_end(html, end_open)
        if end is None:
            # If we can't find a proper end, abort to avoid corrupting the file
            break
        html = html[:start] + html[end:]
        changed = True
    return html


def process_file(path: str) -> bool:
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    updated = remove_div_by_class(original, "left-sidemobile")
    updated = remove_div_by_class(updated, "left-sidedesktop")

    if updated != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
        return True
    return False


def main():
    changed_files = []
    for root, dirs, files in os.walk(ROOT):
        for name in files:
            if not name.endswith(".html"):
                continue
            if name == "nav.html":
                continue
            path = os.path.join(root, name)
            if process_file(path):
                changed_files.append(os.path.relpath(path, ROOT))

    if changed_files:
        print("Removed left-side blocks from:")
        for p in changed_files:
            print(p)
    else:
        print("No changes needed.")


if __name__ == "__main__":
    main()


