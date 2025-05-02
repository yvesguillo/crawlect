#! /usr/bin/env python3

from openai import OpenAI
from ollama import Client

class LLM:
    """LLM class handles standard LLM prompting."""

    def __init__(self):

        # Store the class arguments for __repr__.
        self.args = {}

        # Auto kindness mode attributes.
        self.auto_kind = {}
        self.auto_kind["greetings"] = "Hello!\n"
        self.auto_kind["thanks"] = "Thank you!\n"

        # History.
        self.history = {}
        self.history["messages"] = []
        self.history["responses"] = []

    def request(self, message = None, auto_kind = True):

        # Validate.
        if message is None:
            raise AttributeError(f"\n# Argument error #\n{type(self).__name__}.request requires a prompt message. Got: {repr(message)}.")

        #Auto kindness mode.
        if auto_kind:
            if len(self.history["messages"]) < 1:
                message = self.auto_kind["greetings"] + message
            else:
                message = self.auto_kind["thanks"] + message

        response = self._prompt(message = message)

        self.history["messages"].append(message)
        self.history["responses"].append(response)

        return response

    def _prompt(self, message):
        return f"You sent {repr(message)} to LLM."

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"


######################
# Open AI (Chat GPT) #
######################

class OpenAi(LLM):
    """Extend LLM class for Open AI support."""

    def __init__(self, api_key = None, model = "gpt-4o-mini"):

        # Validate.
        if api_key is None:
            raise AttributeError(f"\n# Argument error #\n{type(self).__name__} requires an Open AI API key.")

        super().__init__()

        # Store the class arguments for __repr__.
        self.args = {}

        # Open AI settings.
        self.api_key = api_key
        self.args["api_key"] = self.api_key
        self.model = model
        self.args["model"] = self.model

        self.client = OpenAI(api_key = api_key)

    def _prompt(self, message):
        completion = self.client.chat.completions.create(
            model = self.model,
            store = True,
            messages = [{"role": "user", "content": message}]
        )

        return completion.choices[0].message


####################
# INTERACTIVE MODE #
####################

if __name__ == "__main__":

    import traceback

    try:

        llm = OpenAi(api_key = "your-openai-key")
        print(llm.request("Test"))
        print(llm.request("Test"))

    except KeyboardInterrupt:
        print("Interupted by user.")

    except Exception as error:
        print(f"\nUnexpected {type(error).__name__}:\n{error}\n")

        # Debug.
        lines = traceback.format_tb(error.__traceback__)
        for line in lines:
            print(line)