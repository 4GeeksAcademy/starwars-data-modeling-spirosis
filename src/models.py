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
    films = Column(String(50), nullable = True)
    url = Column(String(250), unique = True, nullable = False)
    orbital_period = Column(Integer, nullable = False)
    character = relationship('Characters')

class Starships(Base):

    __tablename__ = 'starships'

    starship_id = Column(Integer, primary_key = True )
    name = Column(String(50), unique = True)
    starship_id = Column(Integer, ForeignKey('starship.id'))
    model = Column(String(25), nullable = False)
    manufacture = Column(String(25), nullable = False)
    cost_in_credits = Column(Integer, nullable = False)
    created = Column(String(50), nullable = False)
    crew = Column(Integer, nullable = False)
    max_atmospheric_speed = Column(Integer, nullable = False)
    passengers = Column(Integer, nullable = True)
    edited = Column(String(25), nullable = False)
    hyperdrive_rating = Column(Integer, nullable = False)
    consumables = Column(Integer, nullable = False)
    cargo_capacity = Column(Integer, nullable = False)
    starship_class = Column(String(50))
    description = Column(String(250))
    films = Column(String(50), nullable = True)
    url = Column(String(250), unique = True, nullable = False)
    pilots = Column(Integer, nullable = False)
    character = relationship('Characters')

class Characters(Base):
    __tablename__ = 'characters'

    character_id = Column(Integer, primary_key = True )
    name = Column(String(50), unique = True)
    gender = Column(String(250), nullable = True)
    height = Column(Integer, nullable = False)
    weight = Column(Integer, nullable = False)
    mass = Column(Integer, nullable = False)
    skin_color = Column(String(50), nullable = False)
    eye_color = Column(String(50), nullable = False)
    hair_color = Column(String(50), nullable = False)
    description = Column(String(500), nullable = False)
    films = Column(String(50), nullable = True)
    url = Column(String(250), unique = True, nullable = False)
    planet_id = Column(Integer, ForeignKey('planets.planet.id'))
    planet = relationship('planets')



class Favorites(Base):
    __tablename__ = 'favorites'

    character_id = Column(Integer, ForeignKey('characters.character_id'), nullable = True)
    planet_id = Column(Integer, ForeignKey('planets.planet_id'), nullable = True)
    starship_id = Column(Integer, ForeignKey('starships.starship_id'), nullable = True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable = True)

    character = relationship('Character')
    planet = relationship('Planets')
    starship = relationship('starships')
    user = relationship('User')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
