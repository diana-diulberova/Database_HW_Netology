import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import Publisher, Book, Shop, Stock, Sale
from login import db_login, db_name, db_pass

Base = declarative_base()

DSN = f'postgresql://{db_login}:{db_pass}@localhost:5432/{db_name}'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()


def search_publisher_name():
    query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    query_publisher_name = input("Введите имя издателя: ")
    query_result = query_join.filter(Publisher.publisher_name == query_publisher_name)
    for result in query_result.all():
        print(f'Издатель "{query_publisher_name}" есть в магазине "{result.shop_name}" под id {result.publisher_id}')


def search_publisher_id():
    query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    query_publisher_id = int(input("Введите id издателя: "))
    query_result = query_join.filter(Publisher.publisher_id == query_publisher_id)
    for result in query_result.all():
        print(f'Издатель "{result.query_publisher_name}" есть в магазине "{result.shop_name}" под id {query_publisher_id}')



if __name__ == '__main__':
    search_publisher_name()
    search_publisher_id()


session.close()
