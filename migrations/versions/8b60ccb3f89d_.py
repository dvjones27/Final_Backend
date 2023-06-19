"""empty message

Revision ID: 8b60ccb3f89d
Revises: 45216fa4090b
Create Date: 2023-06-16 07:35:51.512213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b60ccb3f89d'
down_revision = '45216fa4090b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recycling',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('paper', sa.String(length=75), nullable=False),
    sa.Column('paperAmount', sa.Integer(), nullable=False),
    sa.Column('glass', sa.String(length=75), nullable=False),
    sa.Column('glassAmount', sa.Integer(), nullable=False),
    sa.Column('plastic', sa.String(length=75), nullable=False),
    sa.Column('plasticAmount', sa.Integer(), nullable=False),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('waste',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('dishwasher', sa.String(length=75), nullable=False),
    sa.Column('dishwasherLoads', sa.Integer(), nullable=False),
    sa.Column('washer', sa.String(length=75), nullable=False),
    sa.Column('washerLoads', sa.Integer(), nullable=False),
    sa.Column('dryer', sa.String(length=75), nullable=False),
    sa.Column('dryerLoads', sa.Integer(), nullable=False),
    sa.Column('lights', sa.String(length=75), nullable=False),
    sa.Column('lightsNumber', sa.Integer(), nullable=False),
    sa.Column('lightsTime', sa.Integer(), nullable=False),
    sa.Column('hvac', sa.String(length=75), nullable=False),
    sa.Column('hvacTime', sa.Integer(), nullable=False),
    sa.Column('hvacTemp', sa.Integer(), nullable=False),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('water',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('shower', sa.String(length=75), nullable=False),
    sa.Column('showerTime', sa.Integer(), nullable=False),
    sa.Column('washer', sa.String(length=75), nullable=False),
    sa.Column('washerLoads', sa.Integer(), nullable=False),
    sa.Column('dryer', sa.String(length=75), nullable=False),
    sa.Column('dryerLoads', sa.Integer(), nullable=False),
    sa.Column('lights', sa.String(length=75), nullable=False),
    sa.Column('lightsNumber', sa.Integer(), nullable=False),
    sa.Column('lightsTime', sa.Integer(), nullable=False),
    sa.Column('hvac', sa.String(length=75), nullable=False),
    sa.Column('hvacTime', sa.Integer(), nullable=False),
    sa.Column('hvacTemp', sa.Integer(), nullable=False),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('water')
    op.drop_table('waste')
    op.drop_table('recycling')
    # ### end Alembic commands ###
