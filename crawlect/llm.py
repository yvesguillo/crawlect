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

        self.history = {
            "messages": [],
            "responses": []
        }

        self.auto_chat = {
            "opening": f"Hey {self.get_model_name()}!\n",
            "closing": f"\nThank you {self.get_model_name()}!"
        }


    def inject_context(self, codebase):
        """
        Stores the full codebase in memory to use as persistent context across multiple requests.
        This should be called once before sending follow-up prompts.
        """

        if not isinstance(codebase, str):
            raise ValueError("Injected context must be a string.")

        self.context = codebase.strip()

        print("// Injected full codebase context into LLM memory.")


    def request(self, message = None, auto_chat = True):
        if message is None or not isinstance(message, str):
            raise AttributeError(f"\n# Argument error #\n{type(self).__name__}.request requires a prompt message string.")

        message = message.strip()

        # Prepend context if available
        if hasattr(self, "context") and self.context:
            context_block = (
                f"You are a code analysis assistant.\n"
                f"The following codebase was provided previously:\n"
                f"[CODEBASE START]\n{self.context}\n[CODEBASE END]\n\n"
            )
            message = context_block + message

        message = self.auto_chat["opening"] + message + self.auto_chat["closing"]

        response = self._prompt(message=message)
        self.history["messages"].append(message)
        self.history["responses"].append(response)

        return response


    def _prompt(self, history):
        return f"[FAKE RESPONSE from {self.get_model_name()}]\n{history[-1]['content'][:100]}{'…' if len(message) > 100 else ''}\"\n"


    def get_model_name(self):
        return str(self.model).split(":")[0]


    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        parameters = ", ".join(f"{k} = {repr(v)}" for k, v in self.args.items())
        return f"{type(self).__name__}({parameters})"