"""empty message

Revision ID: 1174786e61fc
Revises: 
Create Date: 2020-05-26 23:49:35.253200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1174786e61fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('volunteers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('volunteers')
    # ### end Alembic commands ###