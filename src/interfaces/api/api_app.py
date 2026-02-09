import uvicorn
from fastapi import FastAPI

from src.interfaces.api.router import main_router

app = FastAPI()
app.include_router(main_router)


@app.get("/")
async def root():  # type: ignore
    return {"message": "run"}


async def run_api() -> None:
    """Run the API"""

    config = uvicorn.Config(app, host="0.0.0.0", port=8080)
    server = uvicorn.Server(config)
    await server.serve()
