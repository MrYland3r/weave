from .physics_qa_creator import PhysicsQACreator
from .qa_task_creator import QATaskCreator
from weave.core.registry import task_creator_registry
import logging

logger = logging.getLogger(__name__)

# Register task creators
task_creator_registry.register("physics_qa", PhysicsQACreator)
logger.info("Registered 'physics_qa' task creator.")

task_creator_registry.register("qa", QATaskCreator)
logger.info("Registered 'qa' task creator.")