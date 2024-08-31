from sqlalchemy import (
    String,
    Column,
    DateTime,
    ForeignKey,
    Float,
    Date,
    PrimaryKeyConstraint,
)
from datetime import datetime
from db.db_config import Base


class Instrument(Base):
    __tablename__ = 'instruments'

    ticker = Column(String, primary_key=True)
    isin = Column(String(20), nullable=True)
    full_name = Column(String, nullable=True)
    type_instrument = Column(String, nullable=False)
    engine = Column(String, nullable=False)
    market = Column(String, nullable=False)
    update_dt = Column(DateTime, default=datetime.utcnow)


class Price(Base):
    __tablename__ = 'prices'
    __table_args__ = (PrimaryKeyConstraint("ticker", "date_price", name="price_pk"),)

    ticker = Column(ForeignKey('instruments.ticker', ondelete='CASCADE'), primary_key=True)
    date_price = Column(Date, nullable=False)
    price = Column(Float, nullable=False)