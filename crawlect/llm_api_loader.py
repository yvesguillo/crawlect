#! /usr/bin/env python3

# Conditionnal Imports.
def init_openai():
    from .openai_request import Openai_Request
    return Openai_Request

def init_ollama():
    from .ollama_request import Ollama_Request
    return Ollama_Request

def get_llm_api_class_map():
    return {
        "openai": init_openai,
        "ollama": init_ollama
    }