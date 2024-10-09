from typing import Dict, Any

class PromptTemplateManager:
    def __init__(self):
        self.templates = {}

    def add_template(self, name: str, template: str):
        self.templates[name] = template

    def get_template(self, name: str) -> str:
        return self.templates[name]

    def render_template(self, name: str, **kwargs: Any) -> str:
        template = self.get_template(name)
        return template.format(**kwargs)