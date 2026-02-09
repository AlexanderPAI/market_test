from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.models.base import Base
from src.infrastructure.db.models.mixins import PrimaryKeyMixin, TimestampMixin


class Client(Base, PrimaryKeyMixin, TimestampMixin):
    """Client table"""

    __tablename__ = "clients"

    name: Mapped[str] = mapped_column("name", nullable=False)
    address: Mapped[str] = mapped_column("address", nullable=False)
    orders: Mapped[List["Order"]] = mapped_column("clients", backpopulate="clients")


class Order(Base, PrimaryKeyMixin, TimestampMixin):
    """Order table"""

    __tablename__ = "orders"

    name: Mapped[str] = mapped_column("name", nullable=False)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    client: Mapped["Client"] = relationship("Client", back_populates="orders")
    order_products: Mapped[List["OrderProducts"]] = relationship(
        "Product", back_populate="order"
    )


class Category(Base, PrimaryKeyMixin, TimestampMixin):
    """Category table"""

    __tablename__ = "categories"

    title: Mapped[str] = mapped_column("title", nullable=False)
    products: Mapped[List["Product"]] = relationship(
        "Product", back_populates="category"
    )
    parent_category: Mapped["Category"] = relationship(
        "Category", back_populate="categories"
    )
    child_category: Mapped[List["Category"]] = relationship(
        "Category", back_populate="categories"
    )


class CategoryRels(Base, PrimaryKeyMixin, TimestampMixin):
    """Category Rels table"""

    __tablename__ = "categories_rels"

    parent_category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), nullable=False
    )
    parent_category: Mapped["Category"] = relationship(
        "Category", back_populates="category_rels"
    )

    child_category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), nullable=False
    )
    child_category: Mapped["Category"] = relationship(
        "Category", back_populates="category_rels"
    )


class Product(Base, PrimaryKeyMixin, TimestampMixin):
    """Product table"""

    __tablename__ = "products"

    title: Mapped[str] = mapped_column("title", nullable=False)
    quantity: Mapped[int] = mapped_column(default=0, nullable=False)
    price: Mapped[float] = mapped_column(default=0, nullable=False)
    category_id: Mapped["Category"] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship("Category", back_populates="products")
    order_products: Mapped[List["OrderProducts"]] = relationship(
        "Product", back_populate="products"
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
