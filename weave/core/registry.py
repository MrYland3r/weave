from typing import Dict, Type, TypeVar, List
import importlib
import pkgutil

T = TypeVar('T')

class Registry:
    def __init__(self):
        self._registry: Dict[str, Type[T]] = {}

    def register(self, key: str, cls: Type[T]):
        self._registry[key] = cls

    def get(self, key: str) -> Type[T]:
        if key not in self._registry:
            raise KeyError(f"No item registered with key: {key}")
        return self._registry[key]

    def list(self):
        return list(self._registry.keys())

    def list_providers(self) -> List[str]:  # Add this method
        return list(self._registry.keys())

def load_plugins(package_name: str, base_class: Type[T], registry: Registry):
    package = importlib.import_module(package_name)
    for _, name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f'{package_name}.{name}')
        for item_name in dir(module):
            item = getattr(module, item_name)
            if isinstance(item, type) and issubclass(item, base_class) and item != base_class:
                registry.register(name, item)

# Create registries
data_provider_registry = Registry()
task_creator_registry = Registry()
llm_provider_registry = Registry()

# Load plugins
# Uncomment these lines when the respective modules are ready
# load_plugins('weave.data_providers', DataProvider, data_provider_registry)
# load_plugins('weave.task_creators', TaskCreator, task_creator_registry)
# load_plugins('weave.llm_interfaces', LLMProvider, llm_provider_registry)