#! /usr/bin/env python3

# Custom modules.
from .llm import LLM

class LLM_Code_Analysis:
    """Manage analysis request to LLM with context retention."""

    def __init__(self, llm = None, codebase = None):
        # Validate
        if llm is None or not isinstance(llm, LLM):
            raise AttributeError(f"\n# Argument error #\n{type(self).__name__} requires a LLM to interact with.")
        if codebase is None or not isinstance(codebase, str):
            raise AttributeError(f"\n# Argument error #\n{type(self).__name__} requires a codebase string to analyse.")

        self.llm = llm
        self.llm.inject_context(codebase)


    def review(self):
        return self.llm.request(
            "Please return your detailed recommendations about the codebase, organized in Markdown:\n"
            "- Code Optimization\n"
            "- Logic Issues\n"
            "- Good Practices\n"
            "- Code Standards Compliance\n"
        )


    def docstring(self):
        return self.llm.request(
            "Write standard Python docstrings for each class or method.\n"
            "Format:\n"
            "### File: `path/to/file.py`\n"
            "#### Class: `MyClass`\n"
            "```python\n"
            "\"\"\"Google-style docstring\"\"\"\n"
            "```"
        )


    def readme(self):
        return self.llm.request(
            "Write a full `README.md` for the codebase, structured as:\n"
            "- Project Title\n"
            "- Description\n"
            "- Features\n"
            "- Installation\n"
            "- Usage\n"
            "- Examples (if any)\n"
            "- License"
        )