import logging

import uvicorn
from fastapi import FastAPI

from src.config import envs
from src.interfaces.api.router import main_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(main_router)


@app.get("/")
async def root():  # type: ignore
    return {"message": "run"}


async def run_api() -> None:
    """Run the API"""
    logger.info(envs)
    config = uvicorn.Config(app, host="0.0.0.0", port=8080)
    server = uvicorn.Server(config)
    await server.serve()
