import asyncio
import logging

from src.config import envs
from src.interfaces.api.api_app import run_api

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.debug(envs.test_env)
    asyncio.run(run_api())
