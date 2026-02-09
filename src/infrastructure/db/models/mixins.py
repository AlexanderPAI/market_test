from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func


class PrimaryKeyMixin:
    """Primary key mixin"""

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)


class TimestampMixin:
    """Timestamp mixin"""

    created_at: Mapped[datetime] = mapped_column(default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now(), nullable=False
    )
