from .base import LLMProvider
from weave.core.registry import llm_provider_registry
import openai
from typing import Any, Dict, List

class OpenAIProvider(LLMProvider):
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key

    async def generate(self, prompt: str, **kwargs) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            **kwargs
        )
        return response.choices[0].message.content

    async def evaluate(self, data: Dict[str, Any], criteria: Dict[str, Any]) -> Dict[str, Any]:
        # Implement evaluation logic here
        pass

    def get_supported_criteria(self) -> List[str]:
        return ["relevance", "coherence", "factual_accuracy"]

    def get_model_info(self) -> Dict[str, Any]:
        return {
            "name": self.model,
            "provider": "OpenAI",
            "type": "chat_completion"
        }

llm_provider_registry.register("openai", OpenAIProvider)