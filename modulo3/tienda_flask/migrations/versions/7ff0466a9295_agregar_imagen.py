"""Agregar Imagen

Revision ID: 7ff0466a9295
Revises: 8300136dfa6e
Create Date: 2024-11-15 21:15:32.667321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ff0466a9295'
down_revision = '8300136dfa6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('producto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_path', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('producto', schema=None) as batch_op:
        batch_op.drop_column('image_path')

    # ### end Alembic commands ###
