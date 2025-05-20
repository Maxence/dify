"""add file only message feature

Revision ID: 4b88f2b7d0e6
Revises: 923752d42eb6
Create Date: 2025-05-20 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4b88f2b7d0e6'
down_revision = '923752d42eb6'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('app_model_configs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('file_only_message', sa.Text(), nullable=True))


def downgrade():
    with op.batch_alter_table('app_model_configs', schema=None) as batch_op:
        batch_op.drop_column('file_only_message')
