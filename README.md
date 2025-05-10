# Crawlect

**Crawl, Collect & Document Your Codebase in Markdown.**

![Crawlect](images/crawlect.avif)

**Crawlect** is a Python module designed to *crawl* a given directory, *collect* relevant files and contents, and *document* the entire structure in a clean, readable Markdown file.

Whether you're analyzing someone else's code or sharing your own, Crawlect makes it effortless to generate a comprehensive project snapshot — complete with syntax-highlighted code blocks, a tree-like structure overview, and fine-tuned filtering rules.

> *Crawlect* is a study project initiated by [*Yves Guillo*](https://yvesguillo.ch) & [*Alexandre Jenzer*](https://github.com/Alex141298), supervised by [*Matthieu Ammiguet*](https://matthieuamiguet.ch/) during [*He-Arc*](https://www.he-arc.ch/en/)'s *CAS-IDD*'s *Python* module (2025).

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

## Getting Started

Crawlect is written in Python and requires minimal setup. Just clone, set up the virtual environment, and you’re ready to document codebases like a Markdown ninja.

### 1. Clone the repo

```bash
git clone https://github.com/yvesguillo/crawlect.git
cd crawlect
```

### 2. Run the setup script

Make it executable first if needed (Linux/macOS):

```bash
chmod +x setup.sh
````

Then run:

```bash
./setup.sh
```

> This script creates a `venv`, activates it, and installs dependencies.

**OR** manually install dependencies:

```bash
pip install -r ./requirements.txt
```

### 3. Run Crawlect

```bash
python -m crawlect.crawlect -p . -o ../digest.md
```

> This will scan the current folder, and generate a Markdown file named `digest.md` in the parent directory.

### 4. Teardown (optional)

When you're done (if you used `setup.sh` script), you can clean everything up with:

```bash
./teardown.sh
```

> This will deactivate and delete the `venv`.

## CLI Options

Here are the most useful options Crawlect understands:

| Options | Description |
|:--|:--|
| `-p`, `--path`, `--path_to_crawl` | Path to crawl (default: current folder `.`) |
| `-o`, `--output`, `--output_file` | Output markdown file name (e.g. `digest.md`) |
| `-op`, `--output_prefix`, `--output_file_prefix` | Prefix for output filename if you want it auto-named |
| `-os`, `--output_suffix`, `--output_file_suffix` | Suffix (usually `.md`) to combine with prefix |
| `-r`, `--recur`, `--recursive_crawling` | Recursive crawling (default: `True`) |
| `-d`, `--depth`, `--recursive_crawling_depth` | Max directory depth (default: infinite) |
| `-crawlig`, `--crawlectignore`, `--crawlectignore_use` | Path to custom ignor file |
| `-gitig`, `--gitignore`, `--gitignore_use` | Use `.gitignore` rules (default: `True`) |
| `-dokig`, `--dockerignore`, `--dockerignore_use` | Use `.dockerignore` rules (default: `True`) |
| `-xen`, `--xenv`, `--sanitize_env_variables` | Sanitize `.env` values (default: `True`) |
| `-tre`, `--tree`, `--visualize_directory_tree` | Include tree structure in output (default: `True`) |

#### Example

```bash
python -m crawlect.crawlect \
  -p ./awesomeproject \
  -o ../digest.md \
  -r yes \
  -d 2 \
  -crawlig ./filetoignore.txt \
  -gitig no \
  -dokig no \
  -xen no \
  -tre yes
```

## How Filtering Works

Crawlect supports standard `.gitignore` filtering. You can use:

- `.crawlectignore` (optional and custom rules — your secret weapon)
- `.gitignore` and `.dockerignore` (auto-detected and parsed like Git would)

These filters follow the [standard `.gitignore` syntax](https://git-scm.com/docs/gitignore), such as:

```gitignore
# Ignore markdown files
*.md

# Ignore the venv folder
venv/

# Ignore one super busy folder except for this very important file.
.git/*
!.git/mysuperimportantfile.love

# Ignore logs, but keep error.log
*.log
!important-error.log
```

Just create a `.crawlectignore` at the root or anywhere and pass it like this:

```bash
python -m crawlect.crawlect -p . -o digest.md -crawlig ../myspecialfolder/.crawlectignore
```

> Bonus: Crawlect will *also* exclude the ignore file itself from the digest, so your `.crawlectignore` won’t show up in the output.

## Example Output

Here's a sneak peek at what Crawlect produces:

````markdown
# my-awesome-project
2025.05.10 14:22

Generated with Crawlect.

## File structure

- **src/**
    - [main.py](#main&period;py)
    - [utils.py](#utils&period;py)

## Files:

### main.py  
[`src/main.py`](src/main.py)

```python
from .utils import un_plus_un

def main():
    print(f"Hello! Did you know that one plus one is strictly similar to \n{un_plus_un()}?")
```

### main.py  
[`src/utils.py`](src/utils.py)

```python
def un_plus_un():
    return "deux"
```
````

## Planned Features (ideas welcome!)
- *LLM* API integration - (*in progress*)
- PIP package
- *HTML* output
- GUI launcher (maybe...)

## Contributing

Got ideas? Found a bug? Want to teach Crawlect how to dance in HTML?

Feel free to fork, star, or open an issue — we're open to collabs and suggestions.

> Friendly contributors get markdown cookies.

## References and thanks

### Markdown code syntax table - From [jincheng9 on GitHub](https://github.com/jincheng9/markdown_supported_languages)

### Argpars boolean argument treatment - From [Codemia](https://codemia.io/knowledge-hub/path/parsing_boolean_values_with_argparse)

### [`gitignore_parser`](https://github.com/mherrmann/gitignore_parser) by [Michael Herrmann](https://github.com/mherrmann/)
