# Import necessary modules
import click
from models import Base, engine, session, PropertyOwner, Property, Tenant

# Create database tables based on ORM models
Base.metadata.create_all(engine)

# Define the CLI group
@click.group()
def cli():
    pass

# Command to add a new property owner
@cli.command()
@click.option('--name', prompt='Enter owner name')
def add_owner(name):
    # Create a new PropertyOwner instance
    owner = PropertyOwner(name=name)
    # Add the owner to the session and commit changes to the database
    session.add(owner)
    session.commit()
    click.echo('Owner added successfully!')

# Command to add a new tenant
@cli.command()
@click.option('--name', prompt='Enter tenant name')
@click.option('--property_id', prompt='Enter property ID')
def add_tenant(name, property_id):
    # Create a new Tenant instance
    tenant = Tenant(name=name, property_id=property_id)
    # Add the tenant to the session and commit changes to the database
    session.add(tenant)
    session.commit()
    click.echo('Tenant added successfully!')

# Command to list all properties
@cli.command()
def list_properties():
    # Query all properties from the database
    properties = session.query(Property).all()
    # Display each property's ID and address
    for prop in properties:
        click.echo(f'Property ID: {prop.id}, Address: {prop.address}')

# Command to list tenants of a specific owner
@cli.command()
@click.option('--owner_id', prompt='Enter owner ID')
def list_tenants(owner_id):
    # Query owner by ID
    owner = session.query(PropertyOwner).filter_by(id=owner_id).first()
    if owner:
        # If owner exists, get their tenants and display their IDs and names
        tenants = owner.tenants
        for tenant in tenants:
            click.echo(f'Tenant ID: {tenant.id}, Name: {tenant.name}')
    else:
        click.echo('Owner not found!')

# Command to delete an owner by ID
@cli.command()
@click.option('--owner_id', prompt='Enter owner ID')
def delete_owner(owner_id):
    # Query owner by ID
    owner = session.query(PropertyOwner).filter_by(id=owner_id).first()
    if owner:
        # If owner exists, delete them from the database
        session.delete(owner)
        session.commit()
        click.echo('Owner deleted successfully!')
    else:
        click.echo('Owner not found!')

# Command to delete a property by ID
@cli.command()
@click.option('--property_id', prompt='Enter property ID')
def delete_property(property_id):
    # Query property by ID
    property = session.query(Property).filter_by(id=property_id).first()
    if property:
        # If property exists, delete it from the database
        session.delete(property)
        session.commit()
        click.echo('Property deleted successfully!')
    else:
        click.echo('Property not found!')

# Command to find an owner by ID
@cli.command()
@click.option('--owner_id', prompt='Enter owner ID')
def find_owner(owner_id):
    # Query owner by ID
    owner = session.query(PropertyOwner).filter_by(id=owner_id).first()
    if owner:
        # If owner exists, display their ID and name
        click.echo(f'Owner ID: {owner.id}, Name: {owner.name}')
    else:
        click.echo('Owner not found!')

# Command to find a property by ID
@cli.command()
@click.option('--property_id', prompt='Enter property ID')
def find_property(property_id):
    # Query property by ID
    property = session.query(Property).filter_by(id=property_id).first()
    if property:
        # If property exists, display its ID and address
        click.echo(f'Property ID: {property.id}, Address: {property.address}')
    else:
        click.echo('Property not found!')


# Execute the CLI commands if the script is run directly
if __name__ == '__main__':
    cli()



