"""
Universal interface for different LLM providers.

This package provides a standardized way to interact with various LLM providers
including OpenAI, Anthropic, Deepseek, and Mistral.
"""

from .client import UniversalLLMClient
from .providers import ProviderType
from .exceptions import AssistantsCoreError, ProviderError, ModelNotSupportedError

__version__ = "0.1.0"
__all__ = [
    "UniversalLLMClient",
    "ProviderType",
    "AssistantsCoreError",
    "ProviderError",
    "ModelNotSupportedError",
]
