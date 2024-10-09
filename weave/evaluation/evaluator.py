from abc import ABC, abstractmethod
from typing import Any, Dict, List
from weave.prompts.template import PromptTemplateManager  # Ensure this import is present

class Evaluator(ABC):
    @abstractmethod
    def evaluate(self, task: Dict[str, Any], response: Any, criteria: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate a response to a task based on given criteria."""
        pass

class LLMEvaluator(Evaluator):
    def __init__(self, llm_provider, prompt_manager: PromptTemplateManager):  # Add prompt_manager parameter
        self.llm_provider = llm_provider
        self.prompt_manager = prompt_manager  # Initialize prompt_manager

    def evaluate(self, task: Dict[str, Any], response: Any, criteria: Dict[str, Any]) -> Dict[str, Any]:
        prompt = self.prompt_manager.render_template("evaluation_prompt", data=task, context=criteria)  # Use prompt_manager
        llm_response = self.llm_provider.generate(prompt)
        return self.parse_evaluation_response(llm_response)

    @abstractmethod
    def generate_evaluation_prompt(self, task: Dict[str, Any], response: Any, criteria: Dict[str, Any]) -> str:
        """Generate a prompt for the LLM to evaluate the response."""
        pass

    @abstractmethod
    def parse_evaluation_response(self, response: str) -> Dict[str, Any]:
        """Parse the LLM's evaluation response into a structured format."""
        pass