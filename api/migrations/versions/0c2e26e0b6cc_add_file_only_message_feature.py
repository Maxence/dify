"""add file_only_message feature"""

Revision ID: 0c2e26e0b6cc
Revises: fecff1c3da27
Create Date: 2025-05-20 00:00:00.000000

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '0c2e26e0b6cc'
down_revision = 'fecff1c3da27'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('app_model_configs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('file_only_message', sa.Text(), nullable=True))


def downgrade():
    with op.batch_alter_table('app_model_configs', schema=None) as batch_op:
        batch_op.drop_column('file_only_message')
