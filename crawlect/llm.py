#! /usr/bin/env python3

class LLM:
    """LLM base class for standardized interaction with any LLM API."""

    def __init__(self, **kwargs):
        self.model = kwargs.get("model", "LLM")

        # Store the class arguments for __repr__.
        self.args = kwargs

        expected = {"host", "api_key", "model"}
        for key in kwargs:
            if key not in expected:
                print(f"Unused LLM parameter: {key} = {kwargs[key]}")

        # Auto chat mode attributes
        self.auto_chat = {
            "opening": f"Hello {self.get_model_name()}!\n",
            "closing": "\n"
        }

        # History
        self.history = {
            "messages": [],
            "responses": []
        }

    def request(self, message = None, auto_chat = True):
        if message is None or not isinstance(message, str):
            raise AttributeError(f"\n# Argument error #\n{type(self).__name__}.request requires a prompt message string.")

        message = message.strip()

        # Auto chat formatting
        if auto_chat:
            message = self.auto_chat["opening"] + message + self.auto_chat["closing"]

        response = self._prompt(message = message)

        self.history["messages"].append(message)
        self.history["responses"].append(response)

        return response

    def _prompt(self, message):
        return f"\nYou sent this to {self.get_model_name()}:\n\"{message[:100]}{'…' if len(message) > 100 else ''}\"\n"

    def get_model_name(self):
        return str(self.model).split(":")[0]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        parameters = ", ".join(f"{k} = {repr(v)}" for k, v in self.args.items())
        return f"{type(self).__name__}({parameters})"