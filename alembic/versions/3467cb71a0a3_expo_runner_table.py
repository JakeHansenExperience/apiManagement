"""expo runner table

Revision ID: 3467cb71a0a3
Revises: eb69a79e5dfb
Create Date: 2023-07-21 15:27:39.531642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3467cb71a0a3'
down_revision = 'eb69a79e5dfb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('expoRunners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('numFloors', sa.Integer(), nullable=True),
    sa.Column('numTickets', sa.Integer(), nullable=True),
    sa.Column('totalTime', sa.Integer(), nullable=True),
    sa.Column('startTime', sa.String(), nullable=True),
    sa.Column('chillinQueue', sa.Integer(), nullable=True),
    sa.Column('bayName', sa.String(), nullable=True),
    sa.Column('runStart', sa.String(), nullable=True),
    sa.Column('onbreak', sa.Boolean(), nullable=True),
    sa.Column('shift', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_expoRunners_id'), 'expoRunners', ['id'], unique=False)
    op.add_column('runners', sa.Column('totalTime', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('runners', 'totalTime')
    op.drop_index(op.f('ix_expoRunners_id'), table_name='expoRunners')
    op.drop_table('expoRunners')
    # ### end Alembic commands ###
