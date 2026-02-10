from typing import List, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.models.base import Base
from src.infrastructure.db.models.mixins import PrimaryKeyMixin, TimestampMixin


class Client(Base, PrimaryKeyMixin, TimestampMixin):
    """Client table"""

    __tablename__ = "clients"

    name: Mapped[str] = mapped_column("name", nullable=False)
    address: Mapped[str] = mapped_column("address", nullable=False)
    orders: Mapped[List["Order"]] = relationship("Order", back_populates="client")


class Order(Base, PrimaryKeyMixin, TimestampMixin):
    """Order table"""

    __tablename__ = "orders"

    client_id: Mapped[Optional[int]] = mapped_column(ForeignKey("clients.id"))
    client: Mapped[Optional["Client"]] = relationship("Client", back_populates="orders")
    order_products: Mapped[List["OrderProducts"]] = relationship(
        "OrderProducts", back_populates="order"
    )


class Category(Base, PrimaryKeyMixin, TimestampMixin):
    """Category table"""

    __tablename__ = "categories"

    title: Mapped[str] = mapped_column("title", nullable=False)
    products: Mapped[List["Product"]] = relationship(
        "Product", back_populates="category"
    )
    children: Mapped[List["Category"]] = relationship(
        "Category", back_populates="parent"
    )
    parent_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=True)
    parent: Mapped["Category"] = relationship(
        "Category",
        remote_side="Category.id",
        back_populates="children",
        foreign_keys=[parent_id],
    )


class Product(Base, PrimaryKeyMixin, TimestampMixin):
    """Product table"""

    __tablename__ = "products"

    title: Mapped[str] = mapped_column("title", nullable=False)
    quantity: Mapped[int] = mapped_column(default=0, nullable=False)
    price: Mapped[float] = mapped_column(default=0, nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=True)
    category: Mapped["Category"] = relationship("Category", back_populates="products")
    order_products: Mapped[List["OrderProducts"]] = relationship(
        "OrderProducts", back_populates="product"
    )


class OrderProducts(Base, PrimaryKeyMixin, TimestampMixin):
    """For m2m relationship Orders - Products"""

    __tablename__ = "order_products"

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    order: Mapped["Order"] = relationship(
        "Order", back_populates="order_products", lazy="selectin"
    )
    product: Mapped["Product"] = relationship(
        "Product", back_populates="order_products", lazy="selectin"
    )
    order_quantity: Mapped[int] = mapped_column(default=0, nullable=False)
