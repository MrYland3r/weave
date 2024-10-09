import openai
from typing import Any, Dict
from weave.llm_interfaces import LLMProvider

class OpenAIProvider(LLMProvider):
    def __init__(self, config: Dict[str, Any]):
        self.model = config.get('model', 'gpt-3.5-turbo')
        openai.api_key = config.get('api_key')

    async def generate(self, prompt: str) -> str:
        response = await openai.ChatCompletion.acreate(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    @classmethod
    def from_config(cls, config: Dict[str, Any]) -> 'OpenAIProvider':
        return cls(config)