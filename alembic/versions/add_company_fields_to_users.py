"""add company fields to users

Revision ID: a1b2c3d4e5f6
Revises: 80e1c127ce32
Create Date: 2026-07-14 22:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, None] = '80e1c127ce32'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('company_name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('company_address', sa.String(), nullable=True))
    op.add_column('users', sa.Column('company_phone', sa.String(), nullable=True))
    op.add_column('users', sa.Column('company_email', sa.String(), nullable=True))
    op.add_column('users', sa.Column('company_logo_url', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'company_logo_url')
    op.drop_column('users', 'company_email')
    op.drop_column('users', 'company_phone')
    op.drop_column('users', 'company_address')
    op.drop_column('users', 'company_name')