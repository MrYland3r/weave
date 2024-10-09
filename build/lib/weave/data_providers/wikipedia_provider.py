import wikipedia
from .text_base import TextDataProvider
from typing import Any, Dict, Optional, List, Tuple

class WikipediaProvider(TextDataProvider):
    def __init__(self, language: str = "en", category: str = None, depth: int = 1):
        super().__init__()
        self.language = language
        self.category = category
        self.depth = depth
        wikipedia.set_lang(language)

    async def fetch(self, **kwargs) -> Optional[Dict[str, Any]]:
        title = kwargs.get("title") or self._get_random_title()
        try:
            page = wikipedia.page(title)
            return {
                "title": page.title,
                "content": page.content,
                "url": page.url,
            }
        except wikipedia.exceptions.DisambiguationError:
            return None

    async def fetch_batch(self, batch_size: int, **kwargs) -> List[Dict[str, Any]]:
        titles = [self._get_random_title() for _ in range(batch_size)]
        return [await self.fetch(title=title) for title in titles]

    async def get_text_content(self, data_point: Dict[str, Any]) -> str:
        return data_point["content"]

    async def generate(self, **kwargs) -> Tuple[Any, Dict[str, Any]]:
        data = await self.fetch(**kwargs)
        if data:
            return data["content"], {"title": data["title"], "url": data["url"]}
        return "", {}

    def _get_random_title(self) -> str:
        if self.category:
            # Removed the second argument 'self.category' as wikipedia.random() only accepts 'count'
            return wikipedia.random(1)[0]
        return wikipedia.random(1)[0]

    @classmethod
    def from_config(cls, config: Dict[str, Any]) -> 'WikipediaProvider':
        return cls(
            language=config.get("language", "en"),
            category=config.get("category"),
            depth=config.get("depth", 1)
        )