"""empty message

Revision ID: a1877add056b
Revises: 
Create Date: 2023-04-25 13:34:51.197016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1877add056b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photo_info',
    sa.Column('Photo id', sa.Integer(), nullable=False),
    sa.Column('Photo size', sa.Integer(), nullable=True),
    sa.Column('Created at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('Photo id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('photo_info')
    # ### end Alembic commands ###