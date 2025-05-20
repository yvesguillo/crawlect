# Crawlect

**Now with *LLM* AI integrated analysis.  
Crawl, Collect & Document Your Codebase in Markdown.**  

![Crawlect](https://raw.githubusercontent.com/yvesguillo/crawlect/main/images/crawlect.avif)

[![PyPI version](https://img.shields.io/pypi/v/crawlect)](https://pypi.org/project/crawlect/)

**Crawlect** is a Python module designed to *crawl* a given directory, *collect* relevant files and contents, *document* the entire structure in a clean, readable Markdown file, and analyze the whole project with *LLM* AI API feedback.

Whether you're analyzing someone else's code or sharing your own, Crawlect makes it effortless to generate a comprehensive project snapshot — complete with syntax-highlighted code blocks, a tree-like structure overview, and fine-tuned filtering rules.

> *Crawlect* is a study project initiated by [*Yves Guillo*](https://yvesguillo.ch) & [*Alexandre Jenzer*](https://github.com/Alex141298), supervised by [*Matthieu Ammiguet*](https://matthieuamiguet.ch/) during [*He-Arc*](https://www.he-arc.ch/en/)'s *CAS-IDD*'s *Python* module (2025).

## Why Crawlect?

When starting with a new project — whether you're reviewing, refactoring, or collaborating — understanding its structure and key files is essential. Crawlect does the heavy lifting by:

- Analyzes your codebase with integrated *LLM* API calls.
- Crawl your project directory (recursively if needed),
- Parsing `.gitignore`/`.dockerignore`/`.crawlectignore` rules to mimic your dev setup,
- Masking sensitive data (like `.env` values),
- Automatically generating a well-organized, shareable `.md` file,
- Embedding file contents in Markdown-formatted code blocks.

## Use cases

- Quickly understand an unfamiliar codebase
- Auto-document your projects
- Share code context with collaborators
- Safely include `.env` files without leaking sensitive values
- Enhancing your workflow with *LLM* code analysis.

***Think of Crawlect as your markdown-minion; obedient, efficient, and allergic to messy folders.***

## Getting Started

Crawlect is written in Python and requires minimal setup. Install the package or clone it to set up the virtual environment, and you’re ready to document codebases like a Markdown ninja.  
Requires **Python 3.10+**

### Install Crawlect via `pip` (The Handy Way™)

Tired of fiddling with virtual environments just to run a CLI tool? We got you.

You can install Crawlect globally in just a few seconds:

```bash
pip install crawlect
```

Then summon your loyal markdown minion from *anywhere* on your system:

```bash
crawlect -p . -o digest.md -open
```

> No clutter, no drama. It just works.

#### Why choose the `pip` route?

* You can call `crawlect` from **any folder** — no need to `cd` into the repo.
* Great for **repeated use** or integrating into your tooling.
* Keeps your system clean (no extra scripts, venvs, or manual installs).

### (Optional) Local Dev Mode

If you're planning to **tinker with Crawlect**, we’ve still got you covered.

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

**OR** manually install requirements.txt:

```bash
pip install -r ./requirements.txt
```

### 3. Run Crawlect

```bash
python -m crawlect -p . -o ../digest.md -open
```

> This scan the current folder and generate a Markdown file named `digest.md` in the parent directory.

### 4. Teardown (optional)

When you're done (if you used `setup.sh` script), you can clean everything up with:

```bash
./teardown.sh
```

> This deactivates and removes the `venv` and optional artifacts.

## CLI Options

Here are the most useful options Crawlect understands:

| Options | Description |
|:--|:--|
| `-p`, `--path` | Path to crawl (default is current folder `.`). |
| `-o`, `--output` | Static output file path (e.g. `./digest.md`). |
| `-op`, `--output_prefix` | Prefix for dynamic output unique file name (e.g. `./digest`). |
| `-os`, `--output_suffix` | Suffix for dynamic output unique file name (e.g. `.md`). |
| `-r`, `--recur` | Enable recursive crawling (default: enabled). Use `--no-recur` to disable. |
| `-d`, `--depth` | Scan depth limit (default is infinite). |
| `--crawlig` | Use .crawlectignore exclusion rules if exist (default: enabled). Use `--no-crawlig` to disable. |
| `--gitig` | Use .gitignore exclusion rules if exist (default: enabled). Use `--no-gitig` to disable. |
| `--dockig` | Use .dockerignore exclusion rules if exist (default: enabled). Use `--no-dockig` to disable. |
| `--xenv` | Sanitize .env variables to mitigate sensitive info leak risk (default: enabled). Use `--no-xenv` to disable. |
| `--tree` | Visualize directory tree in the output file (default: enabled). Use `--no-tree` to disable. |
| `-llmapi`, `--llm-api` | LLM provider to use (e.g., `openai` or `ollama`). |
| `-llmhost`, `--llm-host` | Host URL for the LLM API (only required for Ollama). |
| `-llmkey`, `--llm-api-key` | API key for the LLM (only required for OpenAI). |
| `-llmmod`, `--llm-model` | Model name to use (e.g., `gpt-4.1-nano` or `llama3`). |
| `-llmreq`, `--llm-request` | LLM tasks to perform: `review`, `docstring`, `readme`. |
| `-open`, `--open` | Open the output files once generated (default: disabled). |
| `-verbose`, `--verbose` | Toggle verbosity (default: enabled). Use `--no-verbose` to disable. |

#### Examples

Scan *awesomeproject* folder with 2 depth level scan and write its *digest.md* in parent folder, including a project folder tree, while ignoring `.gitignore` and `.dockerignore` rules but interpreting `.crawlectignore` filtering, without sanitizing `.env` files, then open the generated file with the default system reader.

```bash
crawlect -p ./awesomeproject \
  -o ../digest.md \
  -d 2 \
  --no-gitig no \
  --no-dokig no \
  --no-xenv no \
  -open
```

Scan current folder and write its `digest.md` in parent folder, then request *OpenAi*'s `gpt-4.1-nano` model to review and create docstrings from the codebase.

```bash
crawlect -p . \
  -o ../digest.md \
  --llm-api openai \
  --llm-api-key yoursupersecretkey \
  --llm-model gpt-4 \
  --llm-request review docstring
```

## How LLM Feature Works

Ever wish your code could write its own **README**, explain its quirks, or fill in those long-forgotten **docstrings**?  
With Crawlect’s *LLM-powered analysis*, it can.

### What happens under the hood?

When you add the `--llm-*` parameters to your command, Crawlect does:

1. **Generate the full project digest** as Markdown.
2. **Read that digest** and send it to your favorite LLM (*OpenAI* or *Ollama*, your pick).
3. **Inject it into a custom prompt** depending on your request:
   - `review`: ask the model to review and critique the code.
   - `docstring`: generate docstrings for classes and functions.
   - `readme`: draft a clean, professional README.md based on your project.

The responses are then written to a second file (`<output path>.analysis.md`).

### Supported LLMs

- **Ollama** – Running your own local *Ollama* service?  
  If not, no worry, give a try to this one: [**LLM-Serve**](https://github.com/yvesguillo/llm-serve)  
  Then, simply use `--llm-api ollama`, provide your `--llm-host` (e.g. `http://localhost:11434`), choose your `--llm-model` (e.g., `llama3`) and you are good to go!
- **OpenAI** – Use with `--llm-api openai`, supply your `--llm-api-key`, and pick your `--llm-model` (e.g., `gpt-4.1-nano`).

### Example

Scan current folder and write its *digest.md* in parent folder then request *Ollama* to run a request to *Llama3* model and create README documentation from the codebase.

```bash
crawlect -p . \
  -o ../digest.md \
  --llm-api ollama \
  --llm-host http://localhost:11434 \
  --llm-model llama3 \
  --llm-request readme
```

> Crawlect writes your digest, then generates an `<output path>.analysis.md` file packed with insights.  
> And **Yes!** This *README.md* have been generated like that. Well… with a bit of editing, yet much faster. Spend less time on boilerplate — more on content and *style*.

### Bonus

Crawlect injects the **entire codebase** (in Markdown format) *once*, then asks the LLM to perform each task **with that shared context**. This means:

- No repeated uploads.
- Coherent answers across tasks.
- Responses that actually make sense together.

## How Filtering Works

Crawlect supports standard `.gitignore` filtering. You can use:

- `.crawlectignore` (optional and custom rules — your secret weapon, auto-detected and parsed like Git would)
- `.gitignore` and `.dockerignore` (auto-detected and parsed like Git would)

These filters follow the [standard `.gitignore` syntax](https://git-scm.com/docs/gitignore).

> Bonus: Crawlect *also* exclude the ignore file itself from the digest, so your `.crawlectignore` or any *ignore* file won’t show up in the output unless you choose not to use these.

## Example Output

### Digest

Here's a sneak peek at what Crawlect produces as digest:

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

### utils.py  
[`src/utils.py`](src/utils.py)

```python
def un_plus_un():
    return "deux"
```
````

### Analysis

LLM code analysis looks like that:

```markdown
////////////
// REVIEW //
////////////

<Markdown-formatted review by the LLM>


///////////////
// DOCSTRING //
///////////////

<Auto-generated docstrings with file/class/function structure>


////////////
// README //
////////////

<Markdown README suggestion ready to paste>
```

## Roadmap & Crazy Ideas

- *HTML* output
- GUI launcher (Probably, *Swing* training is coming…)

## Contributing
Got ideas? Spot a bug? Wanna make this thing even cooler?  
Feel free to fork, star, or open an issue — we’d love to hear from you!

## References and thanks

- Markdown code syntax table - From [jincheng9 on GitHub](https://github.com/jincheng9/markdown_supported_languages)
- Argpars boolean argument treatment - From [Codemia](https://codemia.io/knowledge-hub/path/parsing_boolean_values_with_argparse)
- [`gitignore_parser`](https://github.com/mherrmann/gitignore_parser) by [Michael Herrmann](https://github.com/mherrmann/)

If you find Crawlect useful, **give it a ☆** to support the project!  
[![GitHub Repo stars](https://img.shields.io/github/stars/yvesguillo/crawlect?style=social)](#)
