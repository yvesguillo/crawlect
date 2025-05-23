#! /usr/bin/env python3

# Custom modules.
from .llm import LLM

# Standard modules.
from ollama import Client

class Ollama_Request(LLM):
    """Extend LLM class for Ollama support."""

    def __init__(self, **kwargs):
        host = kwargs.get("host")
        model = kwargs.get("model")

        if not isinstance(host, str):
            raise AttributeError(f"{type(self).__name__} requires a 'host' string (e.g.: 'http://localhost:11434').")
        if not isinstance(model, str):
            raise AttributeError(f"{type(self).__name__} requires a 'model' string (e.g.: 'llama3').")

        super().__init__(**kwargs)

        self.client = Client(host = host)


    def _prompt(self, message):
        response = self.client.chat(
            model = self.model,
            messages = [{"role": "user", "content": message}]
        )

        return response['message']['content']