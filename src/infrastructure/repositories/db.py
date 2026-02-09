from typing import Any, Dict, Generic, Optional, Sequence, Type, TypeVar
from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")


class DBRepository(Generic[ModelType]):
    """Database repository"""

    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self._model = model
        self._session = session

    async def get(self, *args: Any, **kwargs: Any) -> Optional[ModelType]:
        """Get entity from the database"""
        statement = select(self._model).filter(*args).filter_by(**kwargs)
        result = await self._session.execute(statement)
        return result.scalars().first()

    async def add(self, obj: Dict[str, Any]) -> ModelType:
        """Add a new entity to the database"""
        db_obj = self._model(**obj)
        self._session.add(db_obj)
        await self._session.commit()
        await self._session.refresh(db_obj)
        return db_obj

    async def update(
        self, obj_id: int | UUID, update_data: Dict[str, Any]
    ) -> Optional[ModelType]:
        """Update an entity from the database"""
        statement = (
            update(self._model)
            .where(getattr(self._model, "id") == obj_id)
            .values(**update_data)
        )
        result = await self._session.execute(statement)
        await self._session.commit()
        await self._session.refresh(result)
        db_obj = result.scalar_one_or_none()
        return db_obj

    async def delete(self, obj_id: int | UUID) -> None:
        """Delete an entity from the database"""
        await self._session.execute(
            delete(self._model).where(getattr(self._model, "id") == obj_id)
        )
        await self._session.commit()

    async def list(self, *args: Any, **kwargs: Any) -> Sequence[ModelType]:
        """List entities from the database"""
        statement = select(self._model)

        if args:
            statement = statement.filter(*args)
        if kwargs:
            statement = statement.filter_by(**kwargs)

        obj_list = await self._session.execute(statement)
        return obj_list.scalars().all()
