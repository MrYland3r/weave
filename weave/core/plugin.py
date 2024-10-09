# weave/weave/core/plugin.py
import importlib
import pkgutil
from typing import Dict, Type, TypeVar, List, Any

T = TypeVar('T')

class PluginRegistry:
    def __init__(self):
        self._plugins = {}

    def register(self, name: str, plugin_cls: Type[Any]):
        self._plugins[name] = plugin_cls

    def get(self, name: str) -> Type[Any]:
        if name not in self._plugins:
            raise KeyError(f"No item registered with key: {name}")
        return self._plugins[name]

    # Add this method to list all registered providers
    def list_providers(self) -> List[str]:
        return list(self._plugins.keys())

def load_plugins(package_name: str, base_class: Type[T]):
    package = importlib.import_module(package_name)
    registry = PluginRegistry()

    for _, name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f'{package_name}.{name}')
        for item_name in dir(module):
            item = getattr(module, item_name)
            if isinstance(item, type) and issubclass(item, base_class) and item != base_class:
                registry.register(name, item)

    return registry