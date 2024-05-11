from models import Session, Owner, Property, Tenant
from models import Session, Base, engine

# Create tables if they don't exist
Base.metadata.create_all(engine)


# Function to add a new owner to the database
def add_owner():
    session = Session()
    name = input("Enter owner's name: ")
    owner = Owner(name=name)
    session.add(owner)
    session.commit()
    print(f"Owner '{name}' added successfully.")

# Function to add a new tenant to a property
def add_tenant():
    session = Session()
    property_id = int(input("Enter property ID for tenant: "))
    property = session.query(Property).filter_by(id=property_id).first()
    if property:
        name = input("Enter tenant's name: ")
        tenant = Tenant(name=name, property_id=property_id)
        session.add(tenant)
        session.commit()
        print(f"Tenant '{name}' added successfully to Property ID {property_id}.")
    else:
        print("Property ID not found.")

# Function to add a new property with an owner
def add_property():
    session = Session()
    address = input("Enter property address: ")
    owner_id = int(input("Enter owner ID for this property: "))
    owner = session.query(Owner).filter_by(id=owner_id).first()
    if owner:
        property = Property(address=address, owner_id=owner_id)
        session.add(property)
        session.commit()
        print(f"Property '{address}' added successfully with Owner ID {owner_id}.")
    else:
        print("Owner ID not found.")

# Function to delete an owner by ID
def delete_owner():
    session = Session()
    owner_id = int(input("Enter owner ID to delete: "))
    owner = session.query(Owner).filter_by(id=owner_id).first()
    if owner:
        session.delete(owner)
        session.commit()
        print(f"Owner with ID {owner_id} deleted successfully.")
    else:
        print("Owner ID not found.")

# Function to delete a property by ID
def delete_property():
    session = Session()
    property_id = int(input("Enter property ID to delete: "))
    property = session.query(Property).filter_by(id=property_id).first()
    if property:
        session.delete(property)
        session.commit()
        print(f"Property with ID {property_id} deleted successfully.")
    else:
        print("Property ID not found.")

# Function to display all owners
def display_owners():
    session = Session()
    owners = session.query(Owner).all()
    if owners:
        print("Owners:")
        for owner in owners:
            print(f"ID: {owner.id}, Name: {owner.name}")
    else:
        print("No owners found.")

# Function to display all properties
def display_properties():
    session = Session()
    properties = session.query(Property).all()
    if properties:
        print("Properties:")
        for property in properties:
            print(f"ID: {property.id}, Address: {property.address}, Owner ID: {property.owner_id}")
    else:
        print("No properties found.")

# Function to display all tenants
def display_tenants():
    session = Session()
    tenants = session.query(Tenant).all()
    if tenants:
        print("Tenants:")
        for tenant in tenants:
            print(f"ID: {tenant.id}, Name: {tenant.name}, Property ID: {tenant.property_id}")
    else:
        print("No tenants found.")

# Function to find an owner by ID
def find_owner():
    session = Session()
    owner_id = int(input("Enter owner ID to find: "))
    owner = session.query(Owner).filter_by(id=owner_id).first()
    if owner:
        print(f"Owner ID: {owner.id}, Name: {owner.name}")
    else:
        print("Owner not found.")

# Function to find a property by ID
def find_property():
    session = Session()
    property_id = int(input("Enter property ID to find: "))
    property = session.query(Property).filter_by(id=property_id).first()
    if property:
        print(f"Property ID: {property.id}, Address: {property.address}, Owner ID: {property.owner_id}")
    else:
        print("Property not found.")

# Function to handle user's choice to view related objects (properties owned by an owner or tenants in a property)
def view_related_objects():
    while True:
        print("\n1. View properties owned by an owner")
        print("2. View tenants in a property")
        print("3. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            owner_id = int(input("Enter owner ID to view properties: "))
            view_properties_by_owner(owner_id)
        elif choice == '2':
            property_id = int(input("Enter property ID to view tenants: "))
            view_tenants_in_property(property_id)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

# Function to view properties owned by an owner
def view_properties_by_owner(owner_id):
    session = Session()
    owner = session.query(Owner).filter_by(id=owner_id).first()
    if owner:
        properties = owner.properties
        if properties:
            print(f"Properties owned by {owner.name}:")
            for property in properties:
                print(f"ID: {property.id}, Address: {property.address}")
        else:
            print(f"No properties found for {owner.name}.")
    else:
        print("Owner not found.")

# Function to view tenants in a property
def view_tenants_in_property(property_id):
    session = Session()
    property = session.query(Property).filter_by(id=property_id).first()
    if property:
        tenants = property.tenants
        if tenants:
            print(f"Tenants in Property ID {property_id}:")
            for tenant in tenants:
                print(f"ID: {tenant.id}, Name: {tenant.name}")
        else:
            print("No tenants found for this property.")
    else:
        print("Property not found.")

# Main function to handle user interaction and menu display
def main():
    while True:
        print("\nWelcome to Real Estate Property Management System")
        print("1. Add Owner")
        print("2. Add Tenant")
        print("3. Add Property")
        print("4. Delete Owner")
        print("5. Delete Property")
        print("6. Display Owners")
        print("7. Display Properties")
        print("8. Display Tenants")
        print("9. Find Owner by ID")
        print("10. Find Property by ID")
        print("11. View Related Objects")
        print("12. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_owner()
        elif choice == '2':
            add_tenant()
        elif choice == '3':
            add_property()
        elif choice == '4':
            delete_owner()
        elif choice == '5':
            delete_property()
        elif choice == '6':
            display_owners()
        elif choice == '7':
            display_properties()
        elif choice == '8':
            display_tenants()
        elif choice == '9':
            find_owner()
        elif choice == '10':
            find_property()
        elif choice == '11':
            view_related_objects()
        elif choice == '12':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()