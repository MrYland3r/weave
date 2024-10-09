# weave/core/framework.py
from typing import List, Dict, Any
from weave.core.config import Config
from weave.data_providers import data_provider_registry
from weave.core.registry import task_creator_registry, llm_provider_registry
from weave.core.task_creator import TaskCreator
from weave.llm_interfaces import LLMProvider

# Add this import to ensure task creators are registered
import weave.task_creators

import logging

logger = logging.getLogger(__name__)

class SyntheticDataFramework:
    def __init__(self, config: Config):
        self.config = config
        self.data_provider = self._load_data_provider()
        self.task_creator = self._load_task_creator()
        self.llm_provider = self._load_llm_provider()

    def _load_data_provider(self):
        provider_name = self.config.get('data_generator.name')
        provider_class = data_provider_registry.get(provider_name)
        return provider_class.from_config(self.config.get('data_generator.params', {}))

    def _load_task_creator(self):
        creator_name = self.config.get('task_creator.name')
        logger.debug(f"Available task creators: {task_creator_registry.list_providers()}")
        creator_class = task_creator_registry.get(creator_name)
        return creator_class(self.llm_provider, self.config.get('task_creator.params', {}))

    def _load_llm_provider(self):
        provider_name = self.config.get('llm_provider.name')
        provider_class = llm_provider_registry.get(provider_name)
        return provider_class(self.config.get('llm_provider.params', {}))

    async def generate_dataset(self, num_samples: int) -> List[Dict[str, Any]]:
        dataset = []
        for _ in range(num_samples):
            data, context = await self.data_provider.generate()
            task = await self.task_creator.create_task(data, context)
            dataset.append(task)
        return dataset

    # Add other methods as needed