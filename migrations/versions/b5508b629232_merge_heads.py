"""merge heads

Revision ID: b5508b629232
Revises: 74f39286e2f6, e8eed7b28de5
Create Date: 2026-03-25 12:44:24.623106

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5508b629232'
down_revision: Union[str, None] = ('74f39286e2f6', 'e8eed7b28de5')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
