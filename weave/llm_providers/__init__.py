from .openai_provider import OpenAIProvider
from weave.core.registry import llm_provider_registry

llm_provider_registry.register("openai", OpenAIProvider)