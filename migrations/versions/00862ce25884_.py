"""empty message

Revision ID: 00862ce25884
Revises: 
Create Date: 2023-05-10 19:16:11.311758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00862ce25884'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transportation',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('travel', sa.String(length=75), nullable=False),
    sa.Column('vehicle', sa.String(length=75), nullable=False),
    sa.Column('fuel', sa.String(length=75), nullable=False),
    sa.Column('carpool', sa.String(length=75), nullable=False),
    sa.Column('miles', sa.String(length=5), nullable=False),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transportation')
    # ### end Alembic commands ###
