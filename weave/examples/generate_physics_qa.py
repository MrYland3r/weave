import asyncio
import os
import logging
from weave.core.framework import SyntheticDataFramework
from weave.core.config import Config

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

async def main():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the config file
    config_path = os.path.join(current_dir, '..', 'config', 'physics_qa_config.json')
    
    # Ensure the config file exists
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    config = Config(config_path)
    logger.debug(f"Loaded config: {config.get_all()}")  # This line should now work
    
    framework = SyntheticDataFramework(config)
    
    num_samples = config.get('num_samples', 10)  # Default to 10 if not specified
    dataset = await framework.generate_dataset(num_samples)
    
    print(f"Generated {len(dataset)} samples")
    if dataset:
        print("Sample data point:")
        print(dataset[0])
    else:
        print("No data points were generated.")

if __name__ == "__main__":
    asyncio.run(main())