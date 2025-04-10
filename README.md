# Crawlect – Crawl, Collect & Document Your Codebase in Markdown

![Crawlect](images/crawlect.png)

**Crawlect** is a Python module designed to *crawl* a given directory, *collect* relevant files and contents, and *document* the entire structure in a clean, readable Markdown file.

Whether you're analyzing someone else's code or sharing your own, Crawlect makes it effortless to generate a comprehensive project snapshot — complete with syntax-highlighted code blocks, a tree-like structure overview, and fine-tuned filtering rules.

## Why Crawlect?

When starting with a new project — whether you're reviewing, refactoring, or collaborating — understanding its structure and key files is essential. Crawlect does the heavy lifting by:

- Traversing your project directory (recursively if needed),
- Filtering files and directories with powerful inclusion/exclusion rules,
- Masking sensitive data (like `.env` values),
- Embedding file contents in Markdown-formatted code blocks,
- Parsing `.gitignore`/`.dockerignore`/`.crawlectignore` rules to mimic your dev setup,
- Automatically generating a well-organized, shareable `.md` file.

## Use cases

- Quickly understand an unfamiliar codebase
- Auto-document your projects
- Share code context with collaborators (or *LLM*!)
- Safely include `.env` files without leaking sensitive values

***Think of Crawlect as your markdown-minion; obedient, efficient, and allergic to messy folders.***

## Architecture:

```text
                         +-------------------+
                         | CLI OR  py Script |
                         +---------+---------+
                                   |
                     Filters rules |
                      Path Objects |
                                   v
                          +-----------------+
                          | Crawlect        |
                          +--------+--------+
                                   |
                     Filters rules |
                      Path Objects |
                                   |
         +-------------------------+-------------------------+
         |                         |                         |
         v                         v                         v
+-----------------+       +--------------- -+       +-----------------+
| Scan            |       | Format          |       | Output          |
|(List files)     |------>|(Detect type &   |------>|(Compose final   |
|                 |   |   | insert codebox) |   |   | Markdown file)  |
+-----------------+   |   +-----------------+   |   +--------+--------+
                      |                         |            |
                Files to list            Codebox strings     |
                 (Obj Paths)              (string (MD))      |
                                                             |
                                   +-------------------------+
                                   |
                                   v
                          +-----------------+
                          | Markdown file   |
                          | --------        |
                          | ---             |
                          +-----------------+
```

- **Crawlect**: Manager class, handles options, sequence, client parameters, and service classes.
- **Scan**: Crawls the directories and applies filtering logic.
- **Format**: Detects file type, builds Markdown-friendly code blocks.
- **Output**: Generates the final `.md` file.

## Crawlect – User Guide
**Crawlect**, the tool that turns your project folder into a beautifully structured Markdown digest — effortlessly.

## Installation
Crawlect currently runs as a standalone module. To use it, simply clone the repo or copy the files:

```bash
git clone https://github.com/yvesguillo/crawlect.git
cd crawlect
python3 crawlect.py
```
*(Packaging for pip? Let us know. We'll help you make it pip-installable!)*

## Quick Start
Generate a Markdown description of the current directory:

```bash
python3 crawlect.py -p . -o ./description.md
```
This will scan the current folder recursively and write a structured `description.md` including the contents of most files.

## Usage Overview
You can run Crawlect via the CLI with plenty of flexible options:

```bash
python3 crawlect.py --path ./my-project --output ./my-doc.md
```
Or dynamically generate unique filenames:

```bash
python3 crawlect.py --path ./my-project --output_prefix ./docs/crawl --output_suffix .md
```
You can filter files and folders:

```bash
# Exclude .png and .jpg files from listing
--excl_ext_li .png .jpg

# Include only .py and .md files for writing
--incl_ext_wr .py .md
```
You can also:

- Limit depth (`--depth 2`)
- Disable recursive crawling (`--recur no`)
- Enable the directory tree overview (`--tree yes`)
- Sanitize .env files (`--xenv yes`)
- Apply `.gitignore`, `.dockerignore`, and `.crawlectignore` files automatically

### Example Command
```bash
python3 crawlect.py \
  --path ./awesome-project \
  --output_prefix ./docs/snapshot \
  --output_suffix .md \
  --excl_ext_li .log .png .jpg \
  --incl_ext_wr .py .json \
  --tree yes \
  --xenv yes
```
Creates a structured markdown file (with a unique name), ignoring noisy files and including `.py` and `.json` contents.

### Tips

- `.env` files are *auto-sanitized*; values are replaced by `YourValueFor_<varname>`
- Inclusion rules overrule exclusion
- File name rules take precedence over extension rules
- `.gitignore`, `.dockerignore`, and `.crawlectignore` are respected if available

### Module Mode

You can use Crawlect as a **Python module** too:

```python
from crawlect import Crawlect

myCrawler = Crawlect(path=".", output="./project_overview.md")
myCrawler.outputService.compose()
```

## Advanced Filtering Features

Crawlect doesn’t just crawl. It **obeys your rules like a good little spider**; deciding which files and folders to list and which to write based on powerful filtering logic.

### How Filtering Works

There are **two phases** of filtering:  
1. **Listing phase** (`_li` suffix): decides which files and folders are shown in the output structure.  
2. **Writing phase** (`_wr` suffix): decides which files have their content embedded in the Markdown output.

You can filter by:
- **File names** (`incl_fil_*`, `excl_fil_*`)
- **File extensions** (`incl_ext_*`, `excl_ext_*`)
- **Directories** (`incl_dir_*`, `excl_dir_*`)

### Rule Hierarchy (Who wins?)
Here’s how Crawlect resolves conflicts:

**FILE NAME RULES** > **EXTENSION RULES** > **DIRECTORY RULES**

For both listing and writing:
- Inclusion always overrules exclusion at the same level
- File name rules take precedence over extension rules
- If no rules? Crawlect lets everything in = anarchy mode!

### Ignore Files
Crawlect parses `.gitignore`, `.dockerignore`, and `.crawlectignore` files:
- Any matching path will be excluded from both listing and writing
- `.git` folder is also auto-excluded if `.gitignore` is active
- Lines starting with `#` or empty lines are ignored

> **Note:** Advanced `.gitignore` syntax like `!pattern` is currently not supported (yet!)

### Examples

List all files except `.jpg` and `.png`:
```bash
--excl_ext_li .jpg .png
```

Only list `.py` and `.md` files:
```bash
--incl_ext_li .py .md
```

List everything except `node_modules` directory:
```bash
--excl_dir_li node_modules
```

Write only `.py` and `README.md` contents:
```bash
--incl_ext_wr .py --incl_fil_wr README.md
```

### Pro tip
You can combine filters creatively. Want to list all `.py` files **except** one specific script?

```bash
--incl_ext_li .py --excl_fil_li evil_script.py
```

Voilà; precise, elegant, and slightly obsessive. Just like your code should be.

## Planned Features (ideas welcome!)
- *Git* related filtering
- *HTML* output
- *LLM* API integration
- Optional syntax highlighting themes
- GUI launcher (maybe...)

## References and thanks

### Markdown code syntax table - From [jincheng9 on GitHub](https://github.com/jincheng9/markdown_supported_languages)

### Argpars boolean argument treatment - From [Codemia](https://codemia.io/knowledge-hub/path/parsing_boolean_values_with_argparse)
