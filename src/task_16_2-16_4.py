# Задание 16.02
# Создать таблицу Студент(Student) с помощью sqlalchemy. Студент
# характеризуется именем(firstname) и фамилией(lastname) и группой к которой
# он приурочен.
# Создать две группы. Добавить в каждую по три студента.

# Задание 16.03
# Создать таблицу Школьный дневник(Diary) с помощью sqlalchemy. Дневник
# характеризуется Средним баллом и студентом к которому он приурочен.
# Получить всех студентов и создать для каждого дневник

# Задание 16.04
# Создать таблицу Книга(Book) с помощью sqlalchemy. Книга характеризуется
# названием, количеством страниц и студентами у которых эта книга.
# Создать 5 книг. Получить всех студентов и добавить каждому студенту эти
# пять книг.

from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
# from sqlalchemy import Table
from sqlalchemy_utils import create_database, database_exists

DB_USER = 'postgres'
DB_PASSWORD = '159koplja'
DB_NAME = '3'
DB_ECHO = True
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}'
                       f'@localhost/{DB_NAME}', echo=True)

if not database_exists(engine.url):
    create_database(engine.url)
Base = declarative_base()


# Задание 16_02
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


# Задание 16_03
class Diary(Base):
    __tablename__ = 'diary'
    id = Column(Integer, primary_key=True)
    sr_ball = Column(String)
    # one-to-one(16_03)
    students = relationship("Students", back_populates="diary", uselist=False)


# Задание 16_04
# association_table = Table('association', Base.metadata,
#                           Column('student_id', Integer,
#                           ForeignKey('student.id')),
#                           Column('book_id', Integer,
#                           ForeignKey('book.id'))
#                           )
#
#
# class Book(Base):
#     __tablename__ = 'book'
#     id = Column(Integer, primary_key=True)
#     book_name = Column(String)
#     number_page = Column(Integer)
#     # many-to-many(16_04)
#      students = relationship("Students", secondary=association_table,
#                              backref='book')


class Students(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    group = Column(String, ForeignKey('group.name'), nullable=False)
    # 16_03
    diary_id = Column(Integer, ForeignKey('diary.id'))
    # many-to-one(16_02)
    group = relationship('Group', foreign_keys='Students.group',
                         backref='students')


Base.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()
# session.add_all([
#      Book(book_name='Captain Kidd', number_page=230),
#      Book(book_name='The Adventures of Tom Sawyer', number_page=200),
#      Book(book_name='Huckleberry Finn', number_page=110)])
session.add_all([
    Students(first_name='wendy', last_name='Wendy Williams', group='Python'),
    Students(first_name='mary', last_name='Mary Contrary', group='Java'),
    Students(first_name='fred', last_name='Fred Flintstone', group='Python')])
session.add_all([
    Group(name='Python'),
    Group(name='Java')])
session.add_all([
    Diary(sr_ball=5),
    Diary(sr_ball=3),
    Diary(sr_ball=9)])
session.commit()
# Base.metadata.drop_all(engine)
