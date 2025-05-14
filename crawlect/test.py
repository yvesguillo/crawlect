import traceback
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

from llm import LLM

try:
##################################################################################

    codebase = "def one_plus_one():\n    return \"deux\""

    llm = LLM()

    llm.auto_chat["greetings"] = f"Hello {llm.get_model_name()}! I'm a simple *Python* procedural script intended to help the user about a project codebase. User requested that I work with you about this codebase. I'm not designed to have conversation, so if this is OK with you, I will simply send a request and only expect the answers from you, without wrapping phrases or texts such as greetings or consecutive questions. Here is the codebase we are talking about: [CODEBASE IN MARKDOWN[\n{codebase}\n]]\nHere is the first request:\n"

    print(llm.request("Plup"))


##################################################################################
except KeyboardInterrupt:
    print("Interrupted by user.")

except Exception as error:
    print(f"\nUnexpected {type(error).__name__}:\n{error}\n")

    # Debug.
    lines = traceback.format_tb(error.__traceback__)
    for line in lines:
        print(line)