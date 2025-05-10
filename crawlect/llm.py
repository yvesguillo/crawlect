#! /usr/bin/env python3

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
