#! /usr/bin/env python3

class LLM:
    """LLM class handles standard LLM prompting."""

    def __init__(self):
        self.model = "LLM"

        # Auto chat mode attributes.
        self.auto_chat = {
            # Used only for first prompt.
            "greetings" : f"Hello {self.get_model_name()}!\n",
            # Used to open all new prompt except for first one.
            "opening" : "Thank you!\n",
            # Used to close all prompt.
            "closing" : "\n"
        }

        # History.
        self.history = {
            "messages" : [],
            "responses" : []
        }

        # Store the class arguments for __repr__.
        self.args = {}

    def request(self, message = None, auto_chat = True):

        # Validate.
        if message is None and not isinstance(message, str):
            raise AttributeError(f"\n# Argument error #\n{type(self).__name__}.request requires a prompt message string.")

        # Clean message
        message = message.strip()

        #Auto chat mode.
        if auto_chat:
            if len(self.history["messages"]) < 1:
                message = self.auto_chat["greetings"] + message
            else:
                message = self.auto_chat["opening"] + message + self.auto_chat["closing"]

        response = self._prompt(message = message)

        self.history["messages"].append(message)
        self.history["responses"].append(response)

        return response

    def _prompt(self, message):
        return f"\nYou sent this to {self.get_model_name()}:\n\"{message[0:100]}{"…" if len(message) > 100 else ""}\"\n"

    def get_model_name(self):
        return str(self.model).split(":")[0]

    def get_greetings(self):
        return (
            f"Hello {llm.get_model_name()}! You are a code analysis assistant. The following codebase is provided for review:\n"
            f"[CODEBASE START]\n{codebase}\n[CODEBASE END]\n"
        )

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"