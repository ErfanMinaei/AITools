```markdown
# allFiles Generator – Python Project Dumper

A lightweight Python script that recursively scans a directory, builds a visual file‑tree, and outputs the **full path** and **content** of every text file (skipping irrelevant directories).  
Perfect for documenting a Python project, sharing code structure, or feeding AI context.

---

## ✨ Features

- 📁 **Tree view** – Shows the directory structure, excluding clutter (`.git`, `venv`, `__pycache__`, …).
- 📄 **Full content dump** – For each file, prints its absolute path and full text content.
- 🧹 **Smart skipping** – Ignores binary files (no garbage) and predefined “noise” directories.
- ⚡ **Fast & recursive** – Uses `os.walk` with pruning, so it never even enters excluded folders.
- 🐧 **Ubuntu / Linux ready** – Works on any OS with Python 3.

---

## 📦 Requirements

- **Python 3.6+** (uses standard library only – no external dependencies).

---

## 🚀 Installation

1. **Download the script** – save it as `generate_allfiles.py` in a convenient location.
2. (Optional) Make it executable:
   ```bash
   chmod +x generate_allfiles.py
   ```

That’s it – it’s self‑contained.

---

## 🛠️ Usage

Navigate to the directory you want to document and run:

```bash
cd /path/to/your/project
python3 generate_allfiles.py
```

or, if executable:

```bash
./generate_allfiles.py
```

After a few seconds, a file **`allFiles.txt`** will appear in the current directory containing:

- the absolute path of the root directory,
- a tree of all directories and files (with excluded directories omitted),
- for every remaining file, its full path followed by its content (UTF‑8 text only).

---

## 🎯 Example Output Snippet

```
main directory : /home/user/my_awesome_project

Tree of directories and files:
├── src
│   ├── core
│   │   └── engine.py
│   └── utils.py
├── tests
│   ├── test_core.py
│   └── test_utils.py
└── README.md

full path of file: /home/user/my_awesome_project/src/core/engine.py
def run():
    print("Engine started")

full path of file: /home/user/my_awesome_project/README.md
# My Awesome Project
...
```

---

## ⚙️ Configuration

Open `generate_allfiles.py` with any text editor. Near the top you’ll find two variables:

```python
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
# EXCLUDE_EXTENSIONS = {'.pyc', '.pyo', '.so', '.dll', '.exe'}
```

- **`EXCLUDE_DIRS`** – Add or remove directory names (exact match, case‑sensitive). These folders are **completely ignored** (not shown in the tree, and their contents are never scanned).
- **`EXCLUDE_EXTENSIONS`** (commented out) – If you uncomment it and add extensions, files with those suffixes will be skipped (e.g., `.pyc`). This is useful for avoiding binary or compiled files.

---

## 📝 Notes & Limitations

- **Text encoding** – The script reads files as UTF‑8. If a file is not UTF‑8 (e.g., a binary image or a different encoding), it will be marked as `[Binary file – content not shown]`.
- **Large files** – The script reads entire files into memory. For very large text files (e.g., >100 MB), consider streaming; but for typical source code projects this is rarely an issue.
- **Hidden files** – By default, hidden files (e.g., `.env`, `.gitignore`) are **included**. If you prefer to skip them, add `if entry.startswith('.'): continue` inside the loops.

---

## 🤝 Contributing

Feel free to adapt the script to your needs. If you find a bug or have a suggestion, open an issue or submit a pull request.

---

## 📄 License

This script is provided under the **MIT License**. Use it freely, modify it, and share it.

---

*Happy documenting!*
```
