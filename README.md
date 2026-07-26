# AI Tools

A collection of lightweight Python utilities for working with AI-assisted development. The project currently includes tools for generating project documentation and fetching README files directly from GitHub repositories.

## Features

- 📂 Generate a complete snapshot of any project directory
- 🌳 Export the directory tree
- 📄 Include the contents of all readable text files
- 🚫 Automatically skip binary files
- ⚙️ Exclude common development directories (`.git`, `venv`, `node_modules`, etc.)
- 📥 Fetch README files from multiple GitHub repositories
- 🔍 Automatically detect common default branches (`main`, `master`, `develop`)
- 📝 Save generated documentation to a single output file
- 🚀 No configuration required

## Tools

### Documentor

Scans any directory and generates a `documents.txt` file containing:

- Project directory path
- Directory tree
- Contents of every readable text file
- Binary file detection

### README Fetcher

Downloads the `README.md` file from one or more GitHub repositories and combines them into a single `readme.txt` file.

Supports:

- Repository URLs
- `owner/repository` format
- Automatic branch detection

## Tech Stack

- Python 3
- Requests

## Installation

```bash
git clone <your-repository-url>
cd AITools

pip install requests
```

## Usage

### Generate Project Documentation

```bash
python documentor.py
```

Enter the directory you want to scan when prompted.

Output:

```
documents.txt
```

---

### Fetch GitHub READMEs

```bash
python readmesfetcher.py
```

Enter one or more repository URLs:

```
https://github.com/user/project
https://github.com/another/repository
```

Output:

```
readme.txt
```

## Project Structure

```
.
├── documentor.py
├── readmesfetcher.py
├── documents.txt
├── allFiles.txt
├── README.md
└── .gitignore
```

## Requirements

- Python 3.7+
- requests

Install dependencies:

```bash
pip install requests
```

## Future Improvements

- Export documentation as Markdown or PDF
- Support additional Git providers (GitLab, Bitbucket)
- Recursive README collection
- CLI arguments instead of interactive prompts
- Custom exclude/include patterns
- Parallel README downloads

## License

This project is licensed under the MIT License.