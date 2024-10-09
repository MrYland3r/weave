from typing import Callable, Dict, List

class HookManager:
    def __init__(self):
        self.hooks: Dict[str, List[Callable]] = {}

    def register_hook(self, name: str, callback: Callable):
        if name not in self.hooks:
            self.hooks[name] = []
        self.hooks[name].append(callback)

    def call_hook(self, name: str, **kwargs):
        if name in self.hooks:
            for callback in self.hooks[name]:
                callback(**kwargs)