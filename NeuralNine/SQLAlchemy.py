from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'

    ssn = Column('ssn', Integer, primary_key=True)
    firstname = Column('firstname', String)
    lastname = Column('lastname', String)
    gender = Column('gender', CHAR)
    age = Column('age', Integer)

    def __init__(self, snn, firstname, lastname, gender, age):
        super().__init__()
        self.ssn = snn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f'{self.ssn} {self.firstname} {self.lastname} {self.gender} {self.age}'


class Thing(Base):
    __tablename__ = 'thing'

    tid = Column('tid', Integer, primary_key=True)
    description = Column('description', String)
    owner = Column(Integer, ForeignKey('people.ssn'))

    def __init__(self, tid, description, owner):
        super().__init__()
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f'{self.owner} thinks about {self.description}'


engine = create_engine('sqlite:///mydb.db', echo=True)
Base.metadata.create_all(bind=engine)

Sessoion = sessionmaker(bind=engine)
session = Sessoion()

person = Person(123, 'Adas', 'Niezgodka', 'M', 35)
session.add(person)
session.commit()

person_01 = Person(456, 'NIE', 'ZABIERZESZ', 'K', 28)
person_02 = Person(568, 'JUŻ', 'WIECEJ', 'K', 28)
person_03 = Person(678, 'MOICH', 'DZIECI', 'K', 28)

session.add(person_01)
session.add(person_02)
session.add(person_03)
session.commit()


results = session.query(Person).all()
print(results)

results = session.query(Person).filter(Person.age <= 28)
for result in results:
    print(result)

results = session.query(Person).filter(Person.lastname.like('%DZ%'))
for result in results:
    print(result)

results = session.query(Person).filter(Person.lastname.in_(['WIECEJ', 'MOGĘ', 'ZABRAĆ']))
for result in results:
    print(result)


t1 = Thing(1, "I've been thinking about you", person_01.ssn)
t2 = Thing(2, "I've been thinking about you", person_01.ssn)
t3 = Thing(3, "I've been thinking about you", person_01.ssn)
t4 = Thing(4, "I've been thinking about you", person_02.ssn)
t5 = Thing(5, "I've been thinking about you", person_03.ssn)
session.add(t1)
session.add(t2)
session.add(t3)
session.add(t4)
session.add(t5)
session.commit()


results = session.query(Thing, Person).filter(Thing.owner == Person.ssn).filter(Person.firstname == 'Adas').all()
for result in results:
    print(result)
