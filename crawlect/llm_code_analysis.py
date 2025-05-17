#! /usr/bin/env python3

# Custom modules.
from .llm import LLM

class LLM_Code_Analysis:
    """Manage analysis request to LLM."""

    def __init__(self, llm = None, codebase = None):
        # Validate.
        if llm is None or not isinstance(llm, LLM):
            raise AttributeError(f"\n# Argument error #\n{type(self).__name__} requires a LLM to interact with.")

        if codebase is None or not isinstance(codebase, str):
            raise AttributeError(f"\n# Argument error #\n{type(self).__name__} requires a codebase string to analyse.")

        self.llm = llm
        self.codebase = codebase

        # Alter llm auto_chat.
        self.llm.auto_chat["opening"] = (
            f"Hello {self.llm.get_model_name()}! You are a code analysis assistant. The following codebase is provided for review:\n"
            f"[CODEBASE START]\n{codebase}\n[CODEBASE END]\n"
        )
        self.llm.auto_chat["closing"] = "\n[Instruction: Output should be Markdown only. No comments, no intro phrases.]\n"

    def review(self):
        return self.llm.request(message = (
        "Please return your detailed recommendations about the codebase.\n"
        "\n"
        "Organize your response in the following sections using Markdown headings:\n"
        "- Code Optimization\n"
        "- Logic Issues\n"
        "- Good Practices\n"
        "- Code Standards Compliance\n"
        "\n"
        "Respond in *Markdown* format only.\n"
    ))

    def docstring(self):
        return self.llm.request(message = (
        "Please write standard Python docstrings for each class or method found in the codebase.\n"
        "\n"
        "For each item, provide:\n"
        "- File path\n"
        "- Class or method name\n"
        "- Generated docstring (in Google-style format)\n"
        "\n"
        "Respond using this Markdown format:\n"
        "\n"
        "### File: `path/to/file.py`\n"
        "#### Class: `MyClass`\n"
        "```python\n"
        "\"\"\"[Google-style docstring here]\"\"\"\n"
        "```\n"
    ))

    def readme(self):
        return self.llm.request(message = (
        "Please provide a standard `README.md` file content for this codebase.\n"
        "\n"
        "Structure it with the following sections:\n"
        "- Project Title\n"
        "- Description\n"
        "- Features\n"
        "- Installation\n"
        "- Usage\n"
        "- Examples (if any)\n"
        "- License\n"
        "\n"
        "Respond with the complete content in Markdown format only, suitable for a GitHub public repository.\n"
    ))