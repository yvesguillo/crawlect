#! /usr/bin/env python3

# Custom modules.
from .llm import LLM

# Standard modules.
from openai import OpenAI

class Openai_Request(LLM):
    """Extend LLM class for OpenAI (ChatGPT) support."""

    _default_model = "gpt-4.1-nano"

    def __init__(self, **kwargs):
        api_key = kwargs.get("api_key")
        model = kwargs.get("model", self._default_model)

        if not isinstance(api_key, str):
            raise AttributeError(f"{type(self).__name__} requires an 'api_key' string.")

        kwargs["model"] = model
        super().__init__(**kwargs)

        self.client = OpenAI(api_key = api_key)

    def _prompt(self, message):
        completion = self.client.chat.completions.create(
            model = self.model,
            store = True,
            messages = [{"role": "user", "content": message}]
        )
        return completion.choices[0].message.content