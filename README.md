# Directory Snapshot Generator

A lightweight Python script that scans any directory you specify and generates a single `allFiles.txt` file containing:

- The scanned directory path
- A tree view of the directory structure
- The contents of every readable text file
- Binary files are automatically detected and skipped

The generated `allFiles.txt` is saved **in the directory where the script is executed**, regardless of which directory is scanned.

---

## Features

- ✅ Scan any directory on your computer
- ✅ Interactive path prompt
- ✅ Generates a directory tree
- ✅ Includes contents of all readable text files
- ✅ Skips common development folders
- ✅ Detects binary files automatically
- ✅ No external dependencies

---

## Excluded Directories

The following directories are skipped by default:

- `.git`
- `venv`
- `env`
- `__pycache__`
- `node_modules`
- `.pytest_cache`
- `.mypy_cache`
- `.tox`
- `.eggs`
- `dist`
- `build`

You can customize this list by editing the `EXCLUDE_DIRS` set near the top of the script.

---

## Usage

Run the script:

```bash
python generator.py
```

You'll be prompted to enter the directory to scan:

```
Enter the directory to scan:
```

Examples:

Windows

```
C:\Users\John\Projects\MyProject
```

Linux / macOS

```
/home/john/projects/myproject
```

---

## Output

After scanning, an `allFiles.txt` file will be created **in the same directory where you ran the script**.

For example:

```
generator.py
README.md
allFiles.txt
```

The scanned project itself is **not modified**.

---

## Output Format

The generated file contains:

### 1. Root directory

```
Main directory:
/path/to/project
```

### 2. Directory tree

```
├── src
│   ├── app.py
│   └── utils.py
├── README.md
└── requirements.txt
```

### 3. File contents

```
Full path of file:
/path/to/project/src/app.py

<contents of app.py>

Full path of file:
/path/to/project/README.md

<contents of README.md>
```

---

## Binary Files

Binary files (images, videos, executables, compiled libraries, etc.) are not included.

Instead, the output will contain:

```
[Binary file – content not shown]
```

---

## Optional Customization

### Exclude additional directories

Modify the `EXCLUDE_DIRS` set.

### Exclude file extensions

Uncomment and edit:

```python
EXCLUDE_EXTENSIONS = {
    ".pyc",
    ".dll",
    ".exe",
}
```

Then uncomment the extension check inside the file processing loop.

---

## Requirements

- Python 3.7+
- No third-party packages required

---

## Use Cases

This tool is useful for:

- Sharing an entire project with ChatGPT or another AI assistant
- Creating project snapshots
- Documenting project structure
- Reviewing large codebases
- Preparing repositories for AI analysis

---

## License

MIT License