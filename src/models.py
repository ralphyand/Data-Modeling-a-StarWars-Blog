import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class FavoriteCharacters(Base):
    __tablename__ = 'FavoriteCharacters'
    id = Column(Integer, primary_key=True) 
    character_id = Column(Integer, ForeignKey('Character.id'))
    user_id= Column (Integer,  ForeignKey("User.id"))

class Planet(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    
class FavoritePlanets(Base):
    __tablename__ = 'FavoritosPlaneta'
    id = Column(Integer, primary_key=True)
    planeta_id = Column(Integer, ForeignKey('Planet.id'))
    user_id= Column(Integer, ForeignKey("User.id"))


class Users(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    last_name = Column(String(250))
    age= Column(Integer, nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')