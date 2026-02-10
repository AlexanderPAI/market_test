from fastapi import APIRouter

from src.interfaces.api.v1.orders import order_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(order_router)
