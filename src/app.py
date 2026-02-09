import asyncio
import logging

from src.interfaces.api.api_app import run_api

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    asyncio.run(run_api())
