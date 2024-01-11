"""empty message

Revision ID: 73084b2033ec
Revises: 20609aada0c4
Create Date: 2024-01-11 13:45:06.362626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73084b2033ec'
down_revision = '20609aada0c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('date_created',
               existing_type=sa.VARCHAR(),
               type_=sa.DateTime(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('date_created',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               existing_nullable=False)

    op.drop_table('comment')
    # ### end Alembic commands ###