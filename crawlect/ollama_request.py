#! /usr/bin/env python3

from ollama import Client

# Custom modules.
from .llm import LLM

class Ollama_request(LLM):
    """Extend LLM class for Ollama support."""

    def __init__(self, host = None, model = None):

        # Validate.
        if host is None:
            raise AttributeError(f"\n# Argument error #\n{type(self).__name__} requires an Ollama host URL (e.g.: \"http://localhost:11434\"), got {repr(host)}.")

        if model is None:
            raise AttributeError(f"\n# Argument error #\n{type(self).__name__} requires a pulled LLM model (e.g.: \"dolphin-phi\"), got {repr(model)}.")

        super().__init__()

        self.host = host
        self.args["host"] = self.host
        self.model = model
        self.args["model"] = self.model

        self.client = Client(host = host)

    def _prompt(self, message):
        completion = self.client.chat(
            model = self.model,
            messages = [
                {"role": "user", "content": message}
            ]
        )

        return response['message']['content']