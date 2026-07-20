#!/usr/bin/env python3
import os

# ----------------------------------------------------------------------
# Customise this set to exclude any directories you don't want to scan.
# (Names are matched exactly, case-sensitive.)
EXCLUDE_DIRS = {
    ".git",
    "venv",
    "env",
    "__pycache__",
    "node_modules",
    ".pytest_cache",
    ".mypy_cache",
    ".tox",
    ".eggs",
    "dist",
    "build",
}

# Also skip files with these extensions (optional).
# EXCLUDE_EXTENSIONS = {".pyc", ".pyo", ".so", ".dll", ".exe"}
# ----------------------------------------------------------------------


def generate_tree(startpath, prefix=""):
    """
    Recursively build a tree representation, skipping directories in
    EXCLUDE_DIRS. Directories are listed first, then files.
    """
    lines = []

    entries = sorted(os.listdir(startpath))

    dirs = []
    files = []

    for entry in entries:
        full = os.path.join(startpath, entry)

        if os.path.isdir(full):
            if entry not in EXCLUDE_DIRS:
                dirs.append(entry)
        else:
            files.append(entry)

    all_entries = dirs + files

    for i, entry in enumerate(all_entries):
        path = os.path.join(startpath, entry)
        is_last = i == len(all_entries) - 1

        connector = "└── " if is_last else "├── "
        lines.append(prefix + connector + entry)

        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            lines.extend(generate_tree(path, prefix + extension))

    return lines


def get_directory():
    """Prompt the user until a valid directory is entered."""
    while True:
        directory = input("Enter the directory to scan: ").strip().strip('"')

        if not directory:
            print("Please enter a directory.\n")
            continue

        directory = os.path.abspath(os.path.expanduser(directory))

        if os.path.isdir(directory):
            return directory

        print(f"Directory does not exist:\n{directory}\n")


def main():
    target_dir = get_directory()

    # Output is always created where the script is executed
    output_file = os.path.join(os.getcwd(), "allFiles.txt")

    with open(output_file, "w", encoding="utf-8") as out:
        out.write(f"Main directory: {target_dir}\n\n")

        out.write("Tree of directories and files:\n")
        tree_lines = generate_tree(target_dir)
        out.write("\n".join(tree_lines))
        out.write("\n\n")

        for root, dirs, files in os.walk(target_dir):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            for file in files:
                # Uncomment if using EXCLUDE_EXTENSIONS
                # if any(file.endswith(ext) for ext in EXCLUDE_EXTENSIONS):
                #     continue

                filepath = os.path.join(root, file)

                out.write(f"Full path of file: {filepath}\n")

                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        out.write(f.read())
                except UnicodeDecodeError:
                    out.write("[Binary file – content not shown]\n")
                except Exception as e:
                    out.write(f"[Error reading file: {e}]\n")

                out.write("\n")

    print(f"\n✅ Output written to:\n{output_file}")


if __name__ == "__main__":
    main()