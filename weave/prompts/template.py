import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class PromptTemplateManager:
    def __init__(self, templates: Dict[str, str]):
        self.templates = templates
        logger.debug(f"Initialized PromptTemplateManager with templates: {self.templates}")

    def render_template(self, template_name: str, data: Any, context: Dict[str, Any]) -> str:
        logger.debug(f"Attempting to render template: {template_name}")
        template = self.templates.get(template_name)
        if not template:
            logger.error(f"Template '{template_name}' not found. Available templates: {list(self.templates.keys())}")
            raise ValueError(f"Template '{template_name}' not found.")
        return template.format(**data, **context)