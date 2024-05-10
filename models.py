# Import necessary modules for ORM setup
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create base for ORM classes
Base = declarative_base()

# Create database engine
engine = create_engine('sqlite:///property_management.db')

# Create session maker
Session = sessionmaker(bind=engine)

# Create session
session = Session()

# Define PropertyOwner class for property owners
class PropertyOwner(Base):
    __tablename__ = 'property_owners'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Relationship to properties and tenants
    properties = relationship('Property', back_populates='owner')
    tenants = relationship('Tenant', back_populates='owner')

# Define Property class for properties
class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey('property_owners.id'))
    owner = relationship('PropertyOwner', back_populates='properties')

# Define Tenant class for tenants
class Tenant(Base):
    __tablename__ = 'tenants'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    property_id = Column(Integer, ForeignKey('properties.id'))
    owner = relationship('PropertyOwner', back_populates='tenants')