import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    gender = Column(String(30), nullable=False)
    height = Column(String(30), nullable=False)
    mass = Column(String(30), nullable=False)
    hair_color = Column(String(30), nullable=False)
    skin_color = Column(String(30), nullable=False)
    eye_color = Column(String(30), nullable=False)
    birth_year = Column(String(30), nullable=False)
    homeworld = Column(String(30), nullable=False)
    url = Column(String(30), nullable=False)
    pass

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    diameter = Column(String(30), nullable=False)
    rotation_period = Column(String(30), nullable=False)
    orbital_period = Column(String(30), nullable=False)
    gravity = Column(String(30), nullable=False)
    population = Column(String(30), nullable=False)
    climate = Column(String(30), nullable=False)
    terrain = Column(String(30), nullable=False)
    surface_water = Column(String(30), nullable=False)
    url = Column(String(30), nullable=False)
    pass

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(String(30), nullable=False)
    vehicle_class = Column(String(30), nullable=False)
    manufacturer = Column(String(30), nullable=False)
    cost_in_credits = Column(String(30), nullable=False)
    length = Column(String(30), nullable=False)
    crew = Column(String(30), nullable=False)
    passengers = Column(String(30), nullable=False)
    max_atmosphering_speed = Column(String(30), nullable=False)
    cargo_capacity = Column(String(30), nullable=False)
    consumables = Column(String(30), nullable=False)
    films = Column(String(30), nullable=False)
    pilots = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    url = Column(String(30), nullable=False)
    pass

class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    pass

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
