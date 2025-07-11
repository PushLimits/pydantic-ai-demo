from collections.abc import Callable
from typing import cast

from pydantic_ai.models import KnownModelName, Model


# Define builder functions for each model type to encapsulate logic
def _build_openai_model(model_identifier: str, api_key: str | None) -> Model:
    from pydantic_ai.models.openai import OpenAIModel
    from pydantic_ai.providers.openai import OpenAIProvider

    return OpenAIModel(model_identifier, provider=OpenAIProvider(api_key=api_key))


def _build_anthropic_model(model_identifier: str, api_key: str | None) -> Model:
    from pydantic_ai.models.anthropic import AnthropicModel
    from pydantic_ai.providers.anthropic import AnthropicProvider

    return AnthropicModel(model_identifier, provider=AnthropicProvider(api_key=api_key))


def _build_gemini_model(model_identifier: str, api_key: str | None) -> Model:
    from pydantic_ai.models.gemini import GeminiModel, GeminiModelName
    from pydantic_ai.providers.google_gla import GoogleGLAProvider

    return GeminiModel(cast(GeminiModelName, model_identifier), provider=GoogleGLAProvider(api_key=api_key))


def _build_groq_model(model_identifier: str, api_key: str | None) -> Model:
    from pydantic_ai.models.groq import GroqModel, GroqModelName
    from pydantic_ai.providers.groq import GroqProvider

    return GroqModel(cast(GroqModelName, model_identifier), provider=GroqProvider(api_key=api_key))


def _build_mistral_model(model_identifier: str, api_key: str | None) -> Model:
    from pydantic_ai.models.mistral import MistralModel
    from pydantic_ai.providers.mistral import MistralProvider

    return MistralModel(model_identifier, provider=MistralProvider(api_key=api_key))


# Registry mapping prefixes to builder functions
MODEL_BUILDERS: dict[str, Callable[[str, str | None], Model]] = {
    "openai": _build_openai_model,
    "anthropic": _build_anthropic_model,
    "google-gla": _build_gemini_model,
    "groq": _build_groq_model,
    "mistral": _build_mistral_model,
}


def build_model_from_name_and_api_key(model_name: KnownModelName, api_key: str | None = None) -> Model:
    """Builds a model instance from a known model name and an optional API key."""

    parts = model_name.split(":", 1)
    if len(parts) != 2:
        raise ValueError(f"Invalid model name format. Expected 'prefix:model_name', but got '{model_name}'.")

    prefix, model_identifier = parts

    if not model_identifier:
        raise ValueError(f"Model identifier cannot be empty for prefix '{prefix}'.")

    builder = MODEL_BUILDERS.get(prefix)
    if builder is None:
        raise ValueError(f"Unsupported model prefix: '{prefix}'")

    return builder(model_identifier, api_key)
