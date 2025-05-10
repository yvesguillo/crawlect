#! /usr/bin/env python3

from openai import OpenAI

# Custom modules.
from .llm import LLM

class Openai_request(LLM):
    """Extend LLM class for Open AI (Chat GPT) support."""

    _default_model = "gpt-4.1-nano"

    def __init__(self, api_key = None, model = None):

        # Validate.
        if api_key is None:
            raise AttributeError(f"\n# Argument error #\n{type(self).__name__} requires an Open AI API key.")

        if model is None:
            print(f"\n{type(self).__name__} requires a model name, got: {repr(model)}. {repr(self._default_model)} will be used instead.")
            model = self._default_model

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

        return completion.choices[0].message.content