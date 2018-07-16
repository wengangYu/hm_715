"""1

Revision ID: 06dc0028a035
Revises: 1f09fbdfc91a
Create Date: 2018-07-16 13:50:29.020920

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '06dc0028a035'
down_revision = '1f09fbdfc91a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('base')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('base',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('username', mysql.VARCHAR(collation='utf8mb4_bin', length=32), nullable=False),
    sa.Column('password_hash', mysql.VARCHAR(collation='utf8mb4_bin', length=128), nullable=True),
    sa.Column('email', mysql.VARCHAR(collation='utf8mb4_bin', length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('users')
    # ### end Alembic commands ###