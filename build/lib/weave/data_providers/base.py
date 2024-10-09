from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Tuple

class DataProvider(ABC):
    @abstractmethod
    async def fetch(self, **kwargs) -> Optional[Dict[str, Any]]:
        """Fetch a single data point."""
        pass

    @abstractmethod
    async def fetch_batch(self, batch_size: int, **kwargs) -> List[Dict[str, Any]]:
        """Fetch a batch of data points."""
        pass

    @abstractmethod
    async def generate(self, **kwargs) -> Tuple[Any, Dict[str, Any]]:
        """Generate a data point and its context."""
        pass

    @classmethod
    @abstractmethod
    def from_config(cls, config: Dict[str, Any]) -> 'DataProvider':
        """Create a data provider instance from a configuration dictionary."""
        pass