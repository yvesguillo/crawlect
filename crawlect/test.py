import traceback
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

from llm import LLM

try:
##################################################################################

    codebase = "def one_plus_one():\n    return \"deux\""

    llm = LLM()

    llm.auto_chat["greetings"] = (
        f"Hello {llm.get_model_name()}! You are a code analysis assistant. The following codebase is provided for review:\n"
        f"[CODEBASE START]\n{codebase}\n[CODEBASE END]\n"
    )

    llm.auto_chat["opening"] = "Thank you!\n"

    llm.auto_chat["closing"] = "\n[Instruction: Output should be Markdown only. No comments, no intro phrases.]\n"

    print(llm.request(
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

    print(llm.request(
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

    print(llm.request(
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

##################################################################################
except KeyboardInterrupt:
    print("Interrupted by user.")

except Exception as error:
    print(f"\nUnexpected {type(error).__name__}:\n{error}\n")

    # Debug.
    lines = traceback.format_tb(error.__traceback__)
    for line in lines:
        print(line)