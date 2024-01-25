import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from login import db_login, db_name, db_pass

Base = declarative_base()

DSN = f'postgresql://{db_login}:{db_pass}@localhost:5432/{db_name}'
engine = sq.create_engine(DSN)


class Publisher(Base):
    __tablename__ = "publisher"
    publisher_id = sq.Column(sq.Integer, primary_key=True)
    publisher_name = sq.Column(sq.String(length=100), unique=True)


class Book(Base):
    __tablename__ = "book"
    book_id = sq.Column(sq.Integer, primary_key=True)
    book_title = sq.Column(sq.String(length=100))
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey("publisher.publisher_id", nullable=False))

    publisher = relationship(Publisher, backref="book")


class Shop(Base):
    __tablename__ = "shop"
    shop_id = sq.Column(sq.Integer, primary_key=True)
    shop_name = sq.column(sq.string(length=40))


class Stock(Base):
    __tablename__="stock"
    stock_id = sq.Column(sq.Integer, primary_key=True)
    book_id = sq.Column(sq.Integer, sq.ForeignKey("book.book_id"), nullable=False)
    shop_id = sq.Column(sq.Integer, sq.ForeignKey("shop.shop_id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")


class Sale(Base):
    __tablename__ = "sale"
    sale_id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Numeric(20,2), nullable=False)
    sale_data = sq.Column(sq.Date, nullable=False)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey("stock.stock_id", nullable=False))
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref="sale")


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
