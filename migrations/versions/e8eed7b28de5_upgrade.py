"""upgrade

Revision ID: e8eed7b28de5
Revises: 1abd5a654b9a
Create Date: 2026-03-22 01:30:39.523050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8eed7b28de5'
down_revision: Union[str, Sequence[str], None] = '1abd5a654b9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
