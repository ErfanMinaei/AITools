#!/usr/bin/env python3
import os

# ----------------------------------------------------------------------
# Customise this set to exclude any directories you don't want to scan.
# (Names are matched exactly, case-sensitive.)
EXCLUDE_DIRS = {
    '.git',
    'venv',
    'env',
    '__pycache__',
    'node_modules',
    '.pytest_cache',
    '.mypy_cache',
    '.tox',
    '.eggs',
    'dist',
    'build',
}
# Also skip files with these extensions (optional).
# EXCLUDE_EXTENSIONS = {'.pyc', '.pyo', '.so', '.dll', '.exe'}
# ----------------------------------------------------------------------


def generate_tree(startpath, prefix=""):
    """
    Recursively build a tree representation, skipping directories in EXCLUDE_DIRS.
    Directories are listed first, then files.
    """
    lines = []
    entries = sorted(os.listdir(startpath))
    # Separate directories and files, filtering out excluded dirs
    dirs = []
    files = []
    for e in entries:
        full = os.path.join(startpath, e)
        if os.path.isdir(full):
            if e not in EXCLUDE_DIRS:
                dirs.append(e)
            # else: skip entirely (don't list it)
        else:
            files.append(e)
    all_entries = dirs + files

    for i, entry in enumerate(all_entries):
        path = os.path.join(startpath, entry)
        is_last = (i == len(all_entries) - 1)
        connector = "└── " if is_last else "├── "
        lines.append(prefix + connector + entry)

        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            lines.extend(generate_tree(path, prefix + extension))

    return lines


def main():
    cwd = os.getcwd()
    output_file = os.path.join(cwd, "allFiles.txt")

    with open(output_file, "w", encoding="utf-8") as out:
        # 1. Main directory
        out.write(f"main directory : {cwd}\n\n")

        # 2. Tree (excluded directories are omitted)
        out.write("Tree of directories and files:\n")
        tree_lines = generate_tree(cwd)
        out.write("\n".join(tree_lines) + "\n\n")

        # 3. File contents – walk, but prune excluded dirs on the fly
        for root, dirs, files in os.walk(cwd):
            # Remove excluded directories from the walk list
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            for file in files:
                # Optional: skip files by extension
                # if any(file.endswith(ext) for ext in EXCLUDE_EXTENSIONS):
                #     continue

                filepath = os.path.join(root, file)
                out.write(f"full path of file: {filepath}\n")
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                        out.write(content)
                except UnicodeDecodeError:
                    out.write("[Binary file – content not shown]\n")
                except Exception as e:
                    out.write(f"[Error reading file: {e}]\n")
                out.write("\n")   # blank line between files

    print(f"✅ Output written to {output_file}")


if __name__ == "__main__":
    main()