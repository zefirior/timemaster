# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    USER_ID = Column(Integer, primary_key=True)
    USER_BIRTHDAY = Column(Date)
    USER_LOGIN = Column(String(50))
    USER_PASSWD = Column(String(50))
    USER_NAME = Column(String(50))
    USER_SNAME = Column(String(50))


class Ring(Base):
    __tablename__ = 'ring'

    RING_ID = Column(Integer, primary_key=True)
    SOME_OPTION = Column(String(20))
    RING_PATH = Column(String(200), nullable=False)


class Alarm(Base):
    __tablename__ = 'alarm'

    ID = Column(Integer, primary_key=True)
    ALARM_NAME = Column(String(50))
    ALARM_DESC = Column(String(250))
    ALARM_SECOND = Column(Integer)
    ALARM_MINUTE = Column(Integer)
    ALARM_HOUR = Column(Integer)
    ALARM_DAY = Column(Integer)
    USER_ID = Column(ForeignKey(u'user.USER_ID'), nullable=False)
    RING_ID = Column(ForeignKey(u'ring.RING_ID'), nullable=False)

    user = relationship(u'User')
    ring = relationship(u'Ring')
