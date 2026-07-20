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
