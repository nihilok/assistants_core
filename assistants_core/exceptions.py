"""Custom exceptions for assistants_core package."""


class AssistantsCoreError(Exception):
    """Base exception for assistants_core package."""
    pass


class ProviderError(AssistantsCoreError):
    """Exception raised when there's an error with a provider."""
    pass


class ModelNotSupportedError(AssistantsCoreError):
    """Exception raised when a model is not supported by a provider."""
    pass


class ConfigurationError(AssistantsCoreError):
    """Exception raised when there's a configuration issue."""
    pass


class AuthenticationError(AssistantsCoreError):
    """Exception raised when authentication fails."""
    pass