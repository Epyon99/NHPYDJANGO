"""many to many

Revision ID: fa66a47a5bf0
Revises: 7ff0466a9295
Create Date: 2024-11-20 16:34:59.912149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa66a47a5bf0'
down_revision = '7ff0466a9295'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('almacen',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('almacen_producto',
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('almacen_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['almacen_id'], ['almacen.id'], ),
    sa.ForeignKeyConstraint(['producto_id'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('producto_id', 'almacen_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('almacen_producto')
    op.drop_table('almacen')
    # ### end Alembic commands ###
