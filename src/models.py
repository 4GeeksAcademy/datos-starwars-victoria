import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    clave = Column(String(250), nullable=False)
    favoritos = relationship("favoritos", backref="usuario", lazy=True)

class Personaje(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    color_ojos = Column(String(250), nullable=False)
    personaje_favorito = relationship("favoritos", backref="personajes", lazy=True)
    
class Planeta(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    población = Column(String(250), nullable=False)
    territorio = Column(String(250), nullable=False)
    planeta_favorito = relationship("Favoritos", backref="Planeta", lazy=True)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    id_planeta = Column(Integer, ForeignKey("planetas.id"), nullable=True)
    id_personaje = Column(Integer, ForeignKey("personajes.id"), nullable=True)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
