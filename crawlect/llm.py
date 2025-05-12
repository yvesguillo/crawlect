#! /usr/bin/env python3

class LLM:
    """LLM class handles standard LLM prompting."""

    def __init__(self):

        # Store the class arguments for __repr__.
        self.args = {}

        # Auto chat mode attributes.
        self.auto_chat = {}
        self.auto_chat["greetings"] = "Hello!\n"
        self.auto_chat["thanks"] = "Thank you!\n"

        # History.
        self.history = {}
        self.history["messages"] = []
        self.history["responses"] = []

    def request(self, message = None, auto_chat = True):

        # Validate.
        if message is None:
            raise AttributeError(f"\n# Argument error #\n{type(self).__name__}.request requires a prompt message. Got: {repr(message)}.")

        #Auto chat mode.
        if auto_chat:
            if len(self.history["messages"]) < 1:
                message = self.auto_chat["greetings"] + message
            else:
                message = self.auto_chat["thanks"] + message

        response = self._prompt(message = message)

        self.history["messages"].append(message)
        self.history["responses"].append(response)

        return response

    def _prompt(self, message):
        return f"You sent \"{message[0:100]}…\" to LLM."

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        argsString = []
        for arg, value in self.args.items():
            argsString.append(f"{arg} = {repr(value)}")
        parameters = ", ".join(argsString)
        return f"{type(self).__name__}({parameters})"
