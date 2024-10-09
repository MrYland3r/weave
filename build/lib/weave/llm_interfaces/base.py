# weave/weave/llm_interfaces/base.py
from abc import ABC, abstractmethod
from typing import Any, Dict, List  # Added List import

class LLMProvider(ABC):
    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> str:
        """Generate a response based on the given prompt."""
        pass

    @abstractmethod
    async def evaluate(self, data: Dict[str, Any], criteria: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate data based on given criteria."""
        pass

    @abstractmethod
    def get_supported_criteria(self) -> List[str]:
        """Return a list of supported evaluation criteria."""
        pass

    @abstractmethod
    def get_model_info(self) -> Dict[str, Any]:
        """Return information about the LLM model being used."""
        pass