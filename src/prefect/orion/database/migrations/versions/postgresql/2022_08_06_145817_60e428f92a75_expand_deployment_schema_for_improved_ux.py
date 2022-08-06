"""Expand deployment schema for improved ux

Revision ID: 60e428f92a75
Revises: 97e212ea6545
Create Date: 2022-08-06 14:58:17.138505

"""
from alembic import op
import sqlalchemy as sa
import prefect


# revision identifiers, used by Alembic.
revision = "60e428f92a75"
down_revision = "97e212ea6545"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("deployment", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "infra_overrides",
                prefect.orion.utilities.database.JSON(astext_type=sa.Text()),
                server_default="{}",
                nullable=False,
            )
        )
        batch_op.add_column(
            sa.Column(
                "path",
                sa.String(),
                nullable=True,
            )
        )
        batch_op.add_column(
            sa.Column(
                "entrypoint",
                sa.String(),
                nullable=True,
            )
        )


def downgrade():
    with op.batch_alter_table("deployment", schema=None) as batch_op:
        batch_op.drop_column("entrypoint")
        batch_op.drop_column("path")
        batch_op.drop_column("infra_overrides")
