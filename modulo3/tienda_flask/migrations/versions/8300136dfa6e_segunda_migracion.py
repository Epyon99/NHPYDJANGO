"""Segunda migracion

Revision ID: 8300136dfa6e
Revises: 
Create Date: 2024-11-15 20:40:01.393393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8300136dfa6e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('proveedor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('direccion', sa.String(length=200), nullable=True),
    sa.Column('telefono', sa.String(length=15), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('producto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('descripcion', sa.String(length=200), nullable=True),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('proveedor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['proveedor_id'], ['proveedor.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('producto')
    op.drop_table('proveedor')
    # ### end Alembic commands ###
