from abc import abstractmethod
from typing import Dict, Any
from .base import DataProvider

class AudioDataProvider(DataProvider):
    @abstractmethod
    async def get_audio_path(self, data_point: Dict[str, Any]) -> str:
        """Get the path to the audio file for a data point."""
        pass