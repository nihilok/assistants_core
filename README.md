# assistants_core

A universal Python package that provides a standardized interface for different LLM providers including OpenAI, Anthropic, Deepseek, and Mistral.

## Features

- **Universal Interface**: Single API to interact with multiple LLM providers
- **Auto-Detection**: Automatically detect the appropriate provider based on model name
- **Streaming Support**: Stream completions from all supported providers
- **Model Capabilities**: Query model capabilities like context window, function calling support, etc.
- **Error Handling**: Comprehensive error handling with provider-specific exceptions
- **Async Support**: Fully asynchronous API for better performance

## Supported Providers

- **OpenAI**: GPT-3.5, GPT-4 models
- **Anthropic**: Claude 2, Claude 3 models  
- **Deepseek**: Deepseek Chat, Deepseek Coder
- **Mistral**: Mistral models including Mixtral

## Installation

```bash
pip install assistants-core
```

## Quick Start

```python
import asyncio
from assistants_core import UniversalLLMClient

async def main():
    client = UniversalLLMClient()
    
    # Auto-detects provider based on model name
    response = await client.complete(
        messages=["What is the capital of France?"],
        model="gpt-3.5-turbo"
    )
    
    print(response.content)

asyncio.run(main())
```

## Configuration

Set your API keys as environment variables:

```bash
export OPENAI_API_KEY="your-openai-key"
export ANTHROPIC_API_KEY="your-anthropic-key"
export DEEPSEEK_API_KEY="your-deepseek-key"
export MISTRAL_API_KEY="your-mistral-key"
```

Or pass them directly:

```python
from assistants_core import UniversalLLMClient, ProviderType

client = UniversalLLMClient(
    provider=ProviderType.OPENAI,
    api_key="your-api-key"
)
```

## Usage Examples

### Basic Completion

```python
import asyncio
from assistants_core import UniversalLLMClient

async def main():
    client = UniversalLLMClient()
    
    response = await client.complete(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain quantum computing briefly."}
        ],
        model="gpt-3.5-turbo",
        max_tokens=150,
        temperature=0.7
    )
    
    print(f"Response: {response.content}")
    print(f"Provider: {response.provider}")
    print(f"Model: {response.model}")
    print(f"Usage: {response.usage}")

asyncio.run(main())
```

### Streaming Completion

```python
import asyncio
from assistants_core import UniversalLLMClient

async def main():
    client = UniversalLLMClient()
    
    async for chunk in client.stream_complete(
        messages=["Tell me a short story about a robot."],
        model="gpt-3.5-turbo",
        max_tokens=200
    ):
        print(chunk, end="", flush=True)

asyncio.run(main())
```

### Model Capabilities

```python
import asyncio
from assistants_core import UniversalLLMClient

async def main():
    client = UniversalLLMClient()
    
    # Get capabilities for a specific model
    capabilities = client.get_model_capabilities("gpt-4")
    
    print(f"Supports function calling: {capabilities.supports_function_calling}")
    print(f"Context window: {capabilities.context_window}")
    print(f"Max tokens: {capabilities.max_tokens}")
    
    # Get all supported models
    all_models = client.get_supported_models()
    for provider, models in all_models.items():
        print(f"{provider}: {len(models)} models")

asyncio.run(main())
```

### Multiple Providers

```python
import asyncio
from assistants_core import UniversalLLMClient, ProviderType

async def main():
    client = UniversalLLMClient()
    
    question = "What is machine learning?"
    
    # OpenAI
    openai_response = await client.complete(
        messages=[question],
        model="gpt-3.5-turbo"
    )
    
    # Anthropic  
    anthropic_response = await client.complete(
        messages=[question],
        model="claude-3-haiku-20240307"
    )
    
    print(f"OpenAI: {openai_response.content[:100]}...")
    print(f"Anthropic: {anthropic_response.content[:100]}...")

asyncio.run(main())
```

## API Reference

### UniversalLLMClient

Main client class for interacting with LLM providers.

#### Methods

- `complete()`: Generate a completion
- `stream_complete()`: Generate a streaming completion  
- `get_model_capabilities()`: Get model capabilities
- `get_supported_models()`: Get supported models for all providers
- `set_provider()`: Set or change the provider

### Models

- `CompletionRequest`: Request object for completions
- `CompletionResponse`: Response object from completions
- `ModelCapabilities`: Information about model capabilities
- `Message`: Individual message in a conversation

### Providers

- `ProviderType`: Enum of supported providers
- `BaseLLMProvider`: Base class for provider implementations

### Exceptions

- `AssistantsCoreError`: Base exception
- `ProviderError`: Provider-related errors
- `ModelNotSupportedError`: Unsupported model errors
- `AuthenticationError`: Authentication failures
- `ConfigurationError`: Configuration issues

## Development

```bash
git clone https://github.com/nihilok/assistants_core.git
cd assistants_core
pip install -e ".[dev]"
```

Run tests:
```bash
pytest
```

## License

MIT License
