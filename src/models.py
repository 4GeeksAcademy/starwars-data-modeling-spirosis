import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    user_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True)
    email = Column(String(250), nullable = False, unique = True)

   
class Planets(Base):
    __tablename__ = 'planets'

    planet_id = Column(Integer, primary_key = True )
    name = Column(String(50), unique = True)
    diameter = Column(Integer, nullable = True)
    mass = Column(Integer, nullable = True)
    population = Column(Integer, nullable = True)
    rotation_period = Column(Integer, nullable = False)
    climate = Column(String(50), nullable = False)
    terrain = Column(String(50), nullable = False)
    orbital_period = Column(Integer, nullable = False)
    character = relationship('Character')

class Starship(Base):

    __tablename__ = 'starship'

    starship_id = Column(Integer, primary_key = True )
    name = Column(String(50), unique = True)
    starship_id = Column(Integer, ForeignKey('starship.id'))
    model = Column(String(25), nullable = False)
    manufacture = Column(String(25), nullable = False)
    cost_in_credits = Column(Integer, nullable = False)
    created = Column(String(50), nullable = False)
    crew = Column(Integer, nullable = False)
    edited = Column(String(25), nullable = False)
    hyperdrive_rating = Column(Integer, nullable = False)
    consumables = Column(Integer, (25), nullable = False)
    cargo_capacity = Column(Integer, nullable = False)
    starship_class = Column(String(50))
    description = Column(String(250))
    pilots = Column(Integer, nullable = False)
    character = relationship('Character')

class Character(Base):
    __tablename__ = 'character'

    character_id = Column(Integer, primary_key = True )
    name = Column(String(50), unique = True)


class Favorites(Base):
    __tablename__ = 'favorites'

    character_id = Column(Integer, ForeignKey('character.character_id') nullable = True)
    planet_id = Column(Integer, ForeignKey('planets.planet_id'), nullable = True)
    starship_id = Column(Integer, ForeignKey('starship.starship_id'), nullable = True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable = True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
