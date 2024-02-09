"""add table location

Revision ID: 73e1f106102d
Revises: 9dc4c8d58ad4
Create Date: 2024-02-10 00:01:39.919607

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '73e1f106102d'
down_revision: Union[str, None] = '9dc4c8d58ad4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
