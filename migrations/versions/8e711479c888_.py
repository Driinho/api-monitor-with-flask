"""empty message

Revision ID: 8e711479c888
Revises: ba8a0f901594
Create Date: 2023-04-26 14:53:19.243023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e711479c888'
down_revision = 'ba8a0f901594'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('incidente', schema=None) as batch_op:
        batch_op.add_column(sa.Column('endereco_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('endereco_id', 'endereco', ['endereco_id'], ['id'])
        batch_op.drop_column('endereco')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('incidente', schema=None) as batch_op:
        batch_op.add_column(sa.Column('endereco', sa.VARCHAR(length=120), nullable=False))
        batch_op.drop_constraint('endereco_id', type_='foreignkey')
        batch_op.drop_column('endereco_id')

    # ### end Alembic commands ###