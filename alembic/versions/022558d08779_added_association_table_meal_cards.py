"""Added Association Table meal_cards

Revision ID: 022558d08779
Revises: 283305d5933f
Create Date: 2023-12-14 02:57:27.800209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '022558d08779'
down_revision = '283305d5933f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meal_cards',
    sa.Column('meal_card_id', sa.Integer(), nullable=True),
    sa.Column('meal_served', sa.VARCHAR(length=40), nullable=True),
    sa.Column('specifications', sa.VARCHAR(length=40), nullable=True),
    sa.Column('satisfaction_rank', sa.Integer(), nullable=True),
    sa.Column('comments', sa.VARCHAR(length=40), nullable=True),
    sa.Column('barista_id', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['barista_id'], ['baristas.barista_id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['clients.client_id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meal_cards')
    # ### end Alembic commands ###
