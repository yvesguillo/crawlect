# 🕷️ Crawlect – Crawl, Collect & Document Your Codebase in Markdown

**Crawlect** is a Python module designed to *crawl* a given directory, *collect* relevant files and contents, and *document* the entire structure in a clean, readable Markdown file.

Whether you're analyzing someone else's code or sharing your own, Crawlect makes it effortless to generate a comprehensive project snapshot — complete with syntax-highlighted code blocks, a tree-like structure overview, and fine-tuned filtering rules.

## 🧠 Why Crawlect?

When starting with a new project — whether you're reviewing, refactoring, or collaborating — understanding its structure and key files is essential. Crawlect does the heavy lifting by:

- Traversing your project directory (recursively if needed),
- Filtering files and directories with powerful inclusion/exclusion rules,
- Masking sensitive data (like `.env` values),
- Embedding file contents in Markdown-formatted code blocks,
- Automatically generating a well-organized, shareable `.md` file.

## 🚀 Use cases

- 🔍 Quickly understand an unfamiliar codebase
- 📄 Auto-document your own projects
- 💬 Share code context with collaborators (or ChatGPT!)
- 🔐 Safely include `.env` files without leaking sensitive values

✨ ***Think of Crawlect as your markdown-minion — obedient, efficient, and allergic to messy folders.***

## 📘 Crawlect – User Guide
Welcome to **Crawlect**, the tool that turns your project folder into a beautifully structured Markdown digest — effortlessly.

## 🔧 Installation
Crawlect currently runs as a standalone module. To use it, simply clone the repo or copy the files:

```bash
git clone https://github.com/yvesguillo/crawlect.git
cd crawlect
python3 crawlect.py
```
*(Packaging for pip? Let us know. We'll help you make it pip-installable!)*

## 🚀 Quick Start
Generate a Markdown description of the current directory:

```bash
python3 crawlect.py -p . -o ./description.md
```
➡️ This will scan the current folder recursively and write a structured `description.md` including the contents of most files.

## 🎯 Usage Overview
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

### 🧪 Example Command
```bash
python3 crawlect.py \
  --path ./awesome-project \
  --output_prefix ./docs/snapshot \
  --output_suffix .md \
  --excl_ext_li .log .png .jpg \
  --incl_ext_wr .py .md \
  --tree yes \
  --xenv yes
➡️ Creates a structured markdown file (with a unique name), ignoring noisy files and including `.py` and `.md` contents.
```
### 🧠 Tips

- `.env` files are *auto-sanitized* — values are replaced by `YourValueFor_<varname>`
- Inclusion rules overrule exclusion
- File name rules take precedence over extension rules

---

### 🤖 Module Mode

You can use Crawlect as a **Python module** too:

```python
from crawlect import Crawlect

myCrawler = Crawlect(path=".", output="./project_overview.md")
myCrawler.outputService.compose()
```

## 🛠️ Planned Features (ideas welcome!)
- *Git* related filtering.
- *HTML* output
- GitHub-flavored *MD* with preview links
- *LLM* API integration.
- Optional syntax highlighting themes
- GUI launcher (👀 who knows?)

## Architecture:

```text
                          +-------------------+
                          |    User (CLI)     |
                          +--------+----------+
                                   |
                                   v
                       +-----------------------+
                       |      Crawlect()       |  <== Main class
                       +----------+------------+
                                  |
         +------------------------+--------------------------+
         |                        |                          |
         v                        v                          v
  +--------------+       +----------------+         +------------------+
  |  Scan        |       |   Format       |         |     Output       |
  | (List files) |       | (Detect type & |         | (Compose final   |
  |              |       | insert codebox)|         |  Markdown file)  |
  +------+-------+       +--------+-------+         +--------+---------+
         |                        |                          |
         v                        v                          v
   Files to list         Codebox strings            Markdown composition
      (Path)                  (MD)                         (MD)
```

- **Scan**: Crawls the directories based on inclusion/exclusion rules
- **Format**: Detects file type & builds Markdown-friendly code blocks
- **Output**: Writes everything to a nicely structured `.md` file

***"Documentation is like a love letter you write to your future self."***  
*— Damian Conway, I believe. Or some other wise code-wizard.*