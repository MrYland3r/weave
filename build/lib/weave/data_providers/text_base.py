from abc import abstractmethod
from typing import Dict, Any
from .base import DataProvider

class TextDataProvider(DataProvider):
    @abstractmethod
    async def get_text_content(self, data_point: Dict[str, Any]) -> str:
        """Extract text content from a data point."""
        pass