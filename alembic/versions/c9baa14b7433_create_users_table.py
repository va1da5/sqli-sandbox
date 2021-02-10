"""create users table

Revision ID: c9baa14b7433
Revises: 
Create Date: 2021-02-10 20:16:32.763383

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "c9baa14b7433"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String(64), index=False, unique=True, nullable=False),
        sa.Column("created", sa.DateTime, index=False, unique=False, nullable=False),
        sa.Column("admin", sa.Boolean, index=False, unique=False, nullable=False),
    )


def downgrade():
    op.drop_table("users")
