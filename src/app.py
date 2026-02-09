import logging

import uvicorn
from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


app = FastAPI()


@app.get("/")
async def root():  # type: ignore
    return {"message": "run"}


if __name__ == "__main__":
    logger.info("Starting app")
    uvicorn.run(app, host="0.0.0.0", port=8080)
