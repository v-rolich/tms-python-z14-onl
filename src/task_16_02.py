# Создать таблицу Студент(Student) с помощью sqlalchemy. Студент
# характеризуется именем(firstname) и фамилией(lastname) и группой к которой
# он приурочен.
# Создать две группы. Добавить в каждую по три студента.

# Создать таблицу Школьный дневник(Diary) с помощью sqlalchemy. Дневник
# характеризуется Средним баллом и студентом к которому он приурочен.
# Получить всех студентов и создать для каждого дневник

# Создать таблицу Книга(Book) с помощью sqlalchemy. Книга характеризуется
# названием, количеством страниц и студентами у которых эта книга.
# Создать 5 книг. Получить всех студентов и добавить каждому студенту эти
# пять книг.
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy_utils import create_database, database_exists

DB_USER = 'postgres'
DB_PASSWORD = '119920'
DB_NAME = 'task2'
DB_ECHO = True
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}'
                       f'@localhost/{DB_NAME}', echo=True)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class Diary(Base):
    __tablename__ = 'diary'
    id = Column(Integer, primary_key=True)
    average_score = Column(Float)


association_table = Table('association', Base.metadata,
                          Column('student_id', Integer,
                          ForeignKey('student.id')),
                          Column('book_id', Integer,
                          ForeignKey('book.id'))
                          )


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    pages = Column(Integer)
    student = Column(Integer, ForeignKey('student.id'))
    student = relationship('Student', secondary=association_table,
                            backref='book')


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    group = Column(Integer, ForeignKey('group.id'), nullable=False)
    diary_id = Column(Integer, ForeignKey('diary.id'))

    students = relationship('Student', back_populates="diary", uselist=False)
    groupe = relationship('Group', foreign_keys='Student.group', backref='students')


Base.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()
session.add_all([
    Student(firstname='Viktoria', lastname='Yushkevich', group='Python'),
    Student(firstname='Andrey', lastname='Andreev', group='Java'),
    Student(firstname='Ivan', lastname='Ivanov', group='Python')])
session.add_all([
    Group(name='Python'),
    Group(name='Java')])
session.add_all([
    Diary(average_score=5.6),
    Diary(average_score=7.3),
    Diary(average_score=4.1)])
session.add_all([
    Book(name='War and peace', pages='1000'),
    Book(name='Woe from mind', pages='250'),
    Book(name='Dead Souls', pages='340'),
    Book(name='Harry Potter', pages='580'),
    Book(name='Twilight', pages='450')])
session.commit()
