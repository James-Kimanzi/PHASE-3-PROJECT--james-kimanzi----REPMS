from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create a base class for declarative ORM models
Base = declarative_base()

# Create an engine to connect to the SQLite database
engine = create_engine('sqlite:///property_management.db', echo=True)

# Create a session maker to interact with the database
Session = sessionmaker(bind=engine)

# Define the Owner class representing owners of properties
class Owner(Base):
    __tablename__ = 'owners'  # Define the table name in the database
    id = Column(Integer, primary_key=True)  # Primary key column for owner ID
    name = Column(String, nullable=False)  # Column for owner's name
    phone_number = Column(String)  # Column for owner's phone number
    physical_address = Column(String)  # Column for owner's physical address
    occupation = Column(String)  # Column for owner's occupation
    # Define a one-to-many relationship with properties (one owner can have many properties)
    properties = relationship('Property', back_populates='owner')

# Define the Property class representing properties
class Property(Base):
    __tablename__ = 'properties'  # Define the table name in the database
    id = Column(Integer, primary_key=True)  # Primary key column for property ID
    address = Column(String, nullable=False)  # Column for property address
    owner_id = Column(Integer, ForeignKey('owners.id'))  # Foreign key referencing owner ID
    # Define a many-to-one relationship with owners (many properties can belong to one owner)
    owner = relationship('Owner', back_populates='properties')
    # Define a one-to-many relationship with tenants (one property can have many tenants)
    tenants = relationship('Tenant', back_populates='property')

# Define the Tenant class representing tenants in properties
class Tenant(Base):
    __tablename__ = 'tenants'  # Define the table name in the database
    id = Column(Integer, primary_key=True)  # Primary key column for tenant ID
    name = Column(String, nullable=False)  # Column for tenant's name
    phone_number = Column(String)  # Column for tenant's phone number
    physical_address = Column(String)  # Column for tenant's physical address
    property_id = Column(Integer, ForeignKey('properties.id'))  # Foreign key referencing property ID
    # Define a many-to-one relationship with properties (many tenants can be in one property)
    property = relationship('Property', back_populates='tenants')