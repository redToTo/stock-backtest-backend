"""Add parameters_used and portfolio_history to backtest_results

Revision ID: 60cc216b6234
Revises: 
Create Date: 2025-06-26 23:07:43.737187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60cc216b6234'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('backtest_results', schema=None) as batch_op:
        batch_op.add_column(sa.Column('parameters_used', sa.Text(), nullable=True, comment='策略参数JSON'))
        batch_op.add_column(sa.Column('portfolio_history', sa.Text(), nullable=True, comment='每日资产组合历史JSON'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('backtest_results', schema=None) as batch_op:
        batch_op.drop_column('portfolio_history')
        batch_op.drop_column('parameters_used')

    # ### end Alembic commands ###
