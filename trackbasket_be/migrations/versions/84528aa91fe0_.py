"""empty message

Revision ID: 84528aa91fe0
Revises: 0d8ccdaff373
Create Date: 2020-05-30 10:07:52.306028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84528aa91fe0'
down_revision = '0d8ccdaff373'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shopping_lists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('at_risk_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['at_risk_user_id'], ['at_risk_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shopping_lists')
    # ### end Alembic commands ###
