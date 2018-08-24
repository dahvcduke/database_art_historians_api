import os 
import sys
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class Historian(Base):
    __tablename__ = 'historian' 
    id = Column(Integer, primary_key=True)
    historian_id = Column(String())
    name = Column(String())
    date_born = Column(String())
    place_born = Column(String())
    date_died = Column(String())
    place_died = Column(String())
    overview = Column(String())
    home_country = Column(String())
    sources = Column(String())
    bibliography = Column(String())
    other_names = Column(String())
    contributor = Column(String())
    notes = Column(String())
    gender = Column(String())
    subject_area = Column(String())
    path = Column(String())



engine = create_engine('sqlite:///database.db')

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)