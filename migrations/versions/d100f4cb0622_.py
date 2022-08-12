"""empty message

Revision ID: d100f4cb0622
Revises: 0966c2e95ff8
Create Date: 2022-08-08 09:44:50.270906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd100f4cb0622'
down_revision = '0966c2e95ff8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
    sa.PrimaryKeyConstraint('artist_id', 'venue_id')
    )
    op.add_column('artists', sa.Column('image_link', sa.String(length=500), nullable=True))
    op.add_column('artists', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.add_column('artists', sa.Column('looking_talent', sa.Boolean(), nullable=False))
    op.add_column('artists', sa.Column('seek_decription', sa.String(), nullable=True))
    op.add_column('venues', sa.Column('image_link', sa.String(length=500), nullable=True))
    op.add_column('venues', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.add_column('venues', sa.Column('looking_talent', sa.Boolean(), nullable=False))
    op.add_column('venues', sa.Column('seek_decription', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'seek_decription')
    op.drop_column('venues', 'looking_talent')
    op.drop_column('venues', 'website_link')
    op.drop_column('venues', 'image_link')
    op.drop_column('artists', 'seek_decription')
    op.drop_column('artists', 'looking_talent')
    op.drop_column('artists', 'website_link')
    op.drop_column('artists', 'image_link')
    op.drop_table('show')
    # ### end Alembic commands ###
