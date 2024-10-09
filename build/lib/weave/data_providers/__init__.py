from .base import DataProvider
from .text_base import TextDataProvider
from .audio_base import AudioDataProvider
from .registry import data_provider_registry
from .wikipedia_provider import WikipediaProvider
from .audio_file_provider import AudioFileProvider
from .csv_text_provider import CSVTextProvider

__all__ = [
    "DataProvider",
    "TextDataProvider",
    "AudioDataProvider",
    "data_provider_registry",
    "WikipediaProvider",
    "AudioFileProvider",
    "CSVTextProvider",
]

# Register providers
data_provider_registry.register("wikipedia", WikipediaProvider)
data_provider_registry.register("audio_file", AudioFileProvider)
data_provider_registry.register("csv_text", CSVTextProvider)