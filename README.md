# LucidFS

A local filesystem versioning and recovery tool — essentially Git for arbitrary files.

**LucidFS** monitors selected directories, detects file changes, stores previous versions, maintains a change history, generates diffs, and allows older versions of files to be restored.

---

### Features

- Automatic filesystem monitoring
- SHA-256 file hashing
- Content-addressed storage
- Automatic deduplication
- Version history
- File diffs
- File restoration
- JSON metadata and JSONL event history
- CLI interface

---

### Usage
```py
python -m src.cli watch <directory>
python -m src.cli history <file>
python -m src.cli diff <file>
python -m src.cli restore <file> <version>
python -m src.cli status
```

#### Watch

Monitor a directory for file changes:

```
python -m src.cli watch src
```

#### History

View the recorded versions of a file:

```
python -m src.cli history src/test.txt
```

#### Diff

Compare the current version with its previous version:

```
python -m src.cli diff src/test.txt
```

#### Restore

Restore a file to a specific version:

```
python -m src.cli restore src/test.txt <version-hash>
```

#### Status

View LucidFS statistics and tracked files:

```
python -m src.cli status
```

---

### Storage

LucidFS stores its data in:

```
~/.lucidfs/
├── files.json
├── events.jsonl
└── objects/
```
File contents are stored using their **SHA-256** hash as the object identifier. Identical file contents therefore share the same stored object.

`files.json` stores the latest version of tracked files, while `events.jsonl` maintains the historical record of changes.

---

### Project Structure
```
lucidfs/
├── src/
│   ├── hashing.py
│   ├── storage.py
│   ├── metadata.py
│   ├── events.py
│   ├── history.py
│   ├── diff.py
│   ├── watcher.py
│   └── cli.py
├── tests/
└── pyproject.toml
```
---

### Tech Stack

- Python 3.12+
- watchdog
- hashlib
- JSON / JSONL
- TOML
- difflib
- Typer
- Rich
- pytest
- zstandard

### Status

LucidFS is currently under active development.

---
