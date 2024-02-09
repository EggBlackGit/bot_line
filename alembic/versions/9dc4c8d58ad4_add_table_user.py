"""add table user

Revision ID: 9dc4c8d58ad4
Revises: 
Create Date: 2024-02-09 23:44:23.782222

"""
from typing import Sequence, Union

from alembic import op
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import Mapped



# revision identifiers, used by Alembic.
revision: str = '9dc4c8d58ad4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

Base = declarative_base()
class DatetimeMixin:
    @declared_attr
    def created_at(cls) -> Mapped[datetime]:
        return Column(DateTime(timezone=True), server_default=func.now(), nullable=False)  # type: ignore

    @declared_attr
    def updated_at(cls) -> Mapped[datetime]:
        return Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)  # type: ignore

    @declared_attr
    def deleted_at(cls) -> Mapped[datetime]:
        return Column(DateTime(timezone=True), nullable=True)  # type: ignore


class User(Base, DatetimeMixin):
    __tablename__ = "user"

    user_id: int = Column(Integer, primary_key=True, autoincrement=True)  # type: ignore
    name: str = Column(String, nullable=True)  # type: ignore



def upgrade() -> None:
    bind = op.get_bind()
    User.__table__.create(bind=bind)


def downgrade() -> None:
    bind = op.get_bind()
    User.__table__.drop(bind=bind)

