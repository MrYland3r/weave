from typing import Any, Dict, List
from weave.core.task_creator import LLMTaskCreator

class PhysicsQACreator(LLMTaskCreator):
    async def create_task(self, data: Any, context: Dict[str, Any]) -> Dict[str, Any]:
        prompt = self.prompt_manager.render_template("physics_qa_task", data=data, context=context)
        response = await self.llm_provider.generate(prompt)
        return self.parse_response(response)

    def parse_response(self, response: str) -> Dict[str, Any]:
        # Implement parsing logic here
        # For now, let's return a simple dictionary
        return {"question": response, "answer": ""}

    def get_supported_task_types(self) -> List[str]:
        return ["physics_qa"]

# Remove the registration line from here
# task_creator_registry.register("physics_qa", PhysicsQACreator)