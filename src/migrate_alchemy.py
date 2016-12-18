# -*- coding:utf-8 -*-

from sqlalchemy import create_engine, Text, Integer, Column, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.types import Interval, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
import hashlib
import datetime

Base = declarative_base()

engine = create_engine('sqlite:///db/testModel.db', echo=True)
meta = MetaData()

class MixinBase():
    __tablename__ = 'default'
    def printer(self, *args):
        prepare_fields = []
        tablename = self.__tablename__
        for arg in args:
            attr = getattr(self, arg)
            prepare_fields.append((arg, attr.decode('utf-8') if isinstance(attr, str) else attr))
        return u"<{} ({})>".format(tablename.upper(),
                                   u', '.join(u'{}=\'{}\''.format(k, v) for k, v in prepare_fields)
                                   ).encode('cp866')


class User(MixinBase, Base):
# class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    birthday = Column(Date)
    login = Column(Text)
    passwd = Column(Text)
    name = Column(Text)
    sname = Column(Text)

    friend = relationship('Friend', back_populates='user', cascade="all, delete, delete-orphan")
    alarm = relationship('Alarm', back_populates='user', cascade="all, delete, delete-orphan")
    chain = relationship('Chain', back_populates='user', cascade="all, delete, delete-orphan")

    def __repr__(self):
        return self.printer('name', 'sname')


# class Friend(Base):
class Friend(MixinBase, Base):
    __tablename__ = 'friend'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    birthday = Column(Date)
    name = Column(Text)
    sname = Column(Text)

    user = relationship('User', back_populates='friend')

    def __repr__(self):
        return self.printer('name', 'sname')


class Ring(MixinBase, Base):
# class Ring(Base):
    __tablename__ = 'ring'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    something = Column(Text)
    name = Column(Text)
    path = Column(Text)

    alarm = relationship('Alarm', back_populates='ring', cascade="all, delete, delete-orphan")
    alint = relationship('Alint', back_populates='ring', cascade="all, delete, delete-orphan")

    def __repr__(self):
        return self.printer('name', 'path')


class Alarm(MixinBase, Base):
# class Alarm(Base):
    __tablename__ = 'alarm'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(Text)
    desc = Column(Text)
    time = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    ring_id = Column(Integer, ForeignKey('ring.id'), nullable=True)

    user = relationship('User', back_populates='alarm')
    ring = relationship('Ring', back_populates='alarm')

    def __repr__(self):
        return self.printer('name', 'desc', 'time')


class Chain(MixinBase, Base):
# class Chain(Base):
    __tablename__ = 'chain'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    something = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)

    user = relationship('User', back_populates='chain')

    alint = relationship('Alint', back_populates='chain', cascade="all, delete, delete-orphan")

    def __repr__(self):
        return self.printer('something')


# class Alint(Base):
class Alint(MixinBase, Base):
    __tablename__ = 'alint'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    something = Column(Text)
    order = Column(Integer)
    interval = Column(Interval)
    ring_id = Column(Integer, ForeignKey('ring.id'), nullable=True)
    chain_id = Column(Integer, ForeignKey('chain.id'), nullable=True)

    ring = relationship('Ring', back_populates='alint')
    chain = relationship('Chain', back_populates='alint')

    def __repr__(self):
        return self.printer('order', 'interval', 'ring')

Base.metadata.create_all(engine)

# admin = User(
#     user_login = 'admin',
#     user_passwd = hashlib.sha256('8c6976e5').hexdigest()
# )

# Session = sessionmaker(bind=engine)
# session = Session()
# session.add(admin)

# ret_user = session.query(User).filter_by(user_login='admin').first()
# me = User(birthday=datetime.date(1993, 2, 2), login = 'zefirior', passwd=hashlib.sha256('qwe').hexdigest(), name=u'Даниил', sname=u'Галиев')
# print(me)
# session.add(me)
# session.add_all(
#     (User(login = 'admin', passwd=hashlib.sha256('admin').hexdigest(), name=u'admin', sname=u'admin'),
#     User(login = 'ksu', passwd=hashlib.sha256('38153987').hexdigest(), name=u'Ксения', sname=u'Сусарова'),
#     Ring(name='good_morning', path='/path/to/file'))
# )
# session.commit()
