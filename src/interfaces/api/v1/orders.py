from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db.db_connector import get_session
from src.infrastructure.db.models.market import Order
from src.infrastructure.repositories.db import DBRepository

order_router = APIRouter()


@order_router.post("/order")
async def create_order(  # type: ignore
    # order_id: int = Body(..., title="Order ID"),
    # product_id: int = Body(..., title="Product ID"),
    # quantity: int = Body(..., title="Quantity"),
    session: AsyncSession = Depends(get_session),
):
    """Create a new order."""
    order_repo = DBRepository(model=Order, session=session)
    order = await order_repo.add()
    return order
