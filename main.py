from models import Owner, Property, Tenant
import re  # Import regular expression module from python standard library

# Function to validate a name input
def validate_name(name):
    while not re.match(r"^[a-zA-Z ]+$", name.strip()):  # Allows alphabets and spaces only
        print("Invalid name format. Please enter a valid name (alphabets and spaces only).")
        name = input("Enter name again: ")
    return name.strip()

# Function to validate a phone number input
def validate_phone_number(phone_number):
    while not re.match(r"^\d{10,}$", phone_number.strip()): # Requires 10 digits or more for phone number
        print("Invalid phone number format. Please enter a valid 10-digit phone number.")
        phone_number = input("Enter phone number again: ")
    return phone_number.strip()


# Main function to handle user interaction and menu display
def main():
    while True:
        print("\nWelcome to Real Estate Property Management System")
            # Owner Methods
        print("1. Add Owner")
        print("2. Update Owner")
        print("3. Delete Owner")
        print("4. Display Owners")
        print("5. Find Owner by ID")

            # Property Methods
        print("6. Add Property")
        print("7. Update Property")
        print("8. Delete Property")
        print("9. Display Properties")
        print("10. Find Property by ID")

            # Tenant Methods
        print("11. Add Tenant")
        print("12. Update Tenant")
        print("13. Delete Tenant")          
        print("14. Display Tenants")        
        print("15. Find Tenant by ID")

        print("16. View Related Objects")

        print("17. Exit")

        choice = input("Enter your choice: ")

            # Owner Methods
        if choice == '1':
            name = validate_name(input("Enter owner's name: "))
            phone_number = validate_phone_number(input("Enter owner's phone number: "))
            physical_address = input("Enter owner's physical address: ")
            occupation = input("Enter owner's occupation: ")
            Owner.create(name, phone_number, physical_address, occupation)
            print(f"Owner '{name}' added successfully.")

        elif choice == '2':
            try:
                owner_id = int(input("Enter owner ID to update: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for owner ID.")
                continue  # Restart the loop to prompt the user again

            owner = Owner.find_by_id(owner_id)
            if owner:
                # Validate and update name
                while True:
                    name_input = input(f"Enter new name for owner ({owner[1]}), or press Enter to leave unchanged: ")
                    if name_input.strip():  # Check if input is not empty
                        name = validate_name(name_input)
                        break
                    else:
                        name = owner[1]
                        break

                # Validate and update phone number
                while True:
                    phone_input = input(f"Enter new phone number for owner ({owner[2]}), or press Enter to leave unchanged: ")
                    if phone_input.strip():  # Check if input is not empty
                        phone_number = validate_phone_number(phone_input)
                        break
                    else:
                        phone_number = owner[2]
                        break

                physical_address = input(f"Enter new physical address for owner ({owner[3]}), or press Enter to leave unchanged: ")
                occupation = input(f"Enter new occupation for owner ({owner[4]}), or press Enter to leave unchanged: ")

                Owner.update(owner_id, name, phone_number, physical_address, occupation)
                print(f"Owner ID {owner_id} updated successfully.")
            else:
                print("Owner not found.")

        elif choice == '3':
            try:
                owner_id = int(input("Enter owner ID to delete: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for owner ID.")
                continue  # Restart the loop to prompt the user again

            owner = Owner.find_by_id(owner_id)
            if owner:
                Owner.delete(owner_id)                
            else:
                print("Owner not found.")

        elif choice == '4':
            owners = Owner.get_all()
            if owners:
                print("Owners:")
                print("-" * 20)
                for owner in owners:
                    print(f"ID: {owner[0]}")
                    print(f"Name: {owner[1]}") 
                    print(f"Phone Number: {owner[2]}")
                    print(f"Physical Address: {owner[3]}")
                    print(f"Occupation: {owner[4]}")
                    print("-" * 20)  # Separate each owner's details
            else:
                print("No owners found.")

        elif choice == '5':
            try:
                owner_id = int(input("Enter owner ID to find: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for owner ID.")
                continue  # Restart the loop to prompt the user again

            owner = Owner.find_by_id(owner_id)
            if owner:
                print(f"Owner ID: {owner[0]}, Name: {owner[1]}")
            else:
                print("Owner not found.")         

            # Property Methods
        elif choice == '6':
            try:
                address = input("Enter property address: ")
                owner_id = int(input("Enter owner ID for this property: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for owner ID.")
                continue  # Restart the loop to prompt the user again

            owner_id = int(input("Enter owner ID for this property: "))
            Property.create(address, owner_id)
            print(f"Property '{address}' added successfully with Owner ID {owner_id}.")

        elif choice == '7':
            try:
                property_id = int(input("Enter property ID to update: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for property ID.")
                continue  # Restart the loop to prompt the user again

            property = Property.find_by_id(property_id)
            if property:
                address = input(f"Enter new address for property ({property[1]}): ")
                Property.update(property_id, address)
                print(f"Property ID {property_id} updated successfully.")
            else:
                print("Property not found.")

        elif choice == '8':
            try:
                property_id = int(input("Enter property ID to delete: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for property ID.")
                continue  # Restart the loop to prompt the user again

            property = Property.find_by_id(property_id)
            if property:
                Property.delete(property_id)                
            else:
                print("Property not found.")

        elif choice == '9':
            properties = Property.get_all()
            if properties:
                print("Properties:")
                print("-" * 20)
                for property in properties:
                    print(f"ID: {property[0]}")
                    print(f"Address: {property[1]}")
                    print(f"Owner ID: {property[2]}")
                    print("-" * 20)  # Separate each property details
            else:
                print("No properties found.")

        elif choice == '10':
            try:
                property_id = int(input("Enter property ID to find: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for property ID.")
                continue  # Restart the loop to prompt the user again

            property = Property.find_by_id(property_id)
            if property:
                print(f"Property ID: {property[0]}, Address: {property[1]}, Owner ID: {property[2]}")
            else:
                print("Property not found.")


            # Tenant Methods
        elif choice == '11':
            name = validate_name(input("Enter tenant's name: "))
            phone_number = validate_phone_number(input("Enter tenant's phone number: "))
            physical_address = input("Enter tenant's physical address: ")
            property_id = input("Enter property ID for this tenant: ")
            Tenant.create(name, phone_number, physical_address, property_id)
            print(f"Tenant '{name}' added successfully to Property ID {property_id}.")

        elif choice == '12':
            try:
                tenant_id = int(input("Enter tenant ID to update: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for tenant ID.")
                continue  # Restart the loop to prompt the user again

            tenant = Tenant.find_by_id(tenant_id)
            if tenant:
                # Validate and update name
                while True:
                    name_input = input(f"Enter new name for tenant ({tenant[1]}), or press Enter to leave unchanged: ")
                    if name_input.strip():  # Check if input is not empty
                        name = validate_name(name_input)
                        break
                    else:
                        name = tenant[1]
                        break

                # Validate and update phone number
                while True:
                    phone_input = input(f"Enter new phone number for tenant ({tenant[2]}), or press Enter to leave unchanged: ")
                    if phone_input.strip():  # Check if input is not empty
                        phone_number = validate_phone_number(phone_input)
                        break
                    else:
                        phone_number = tenant[2]
                        break

                physical_address = input(f"Enter new physical address for tenant ({tenant[3]}), or press Enter to leave unchanged: ")

                Tenant.update(tenant_id, name, phone_number, physical_address)
                print(f"Tenant ID {tenant_id} updated successfully.")
            else:
                print("Tenant not found.")

        elif choice == '13':
            try:
                tenant_id = int(input("Enter tenant ID to delete: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for tenant ID.")
                continue  # Restart the loop to prompt the user again

            tenant = Tenant.find_by_id(tenant_id)
            if tenant:
                Tenant.delete(tenant_id)                
            else:
                print("Tenant not found.")   
        
        elif choice == '14':
            tenants = Tenant.get_all()
            if tenants:
                print("Tenants:")
                print("-" * 20)
                for tenant in tenants:
                    print(f"ID: {tenant[0]}")
                    print(f"Name: {tenant[1]}")
                    print(f"Phone Number: {tenant[2]}")
                    print(f"Physical Address: {tenant[3]}")
                    print(f"Property ID: {tenant[4]}")
                    print("-" * 20)  # Separate each tenant details
            else:
                print("No tenants found.")      
        
        elif choice == '15':
            try:
                tenant_id = int(input("Enter tenant ID to find: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for tenant ID.")
                continue  # Restart the loop to prompt the user again

            tenant = Tenant.find_by_id(tenant_id)
            if tenant:
                print(f"Tenant ID: {tenant[0]}, Name: {tenant[1]}, Property ID: {tenant[4]}")
            else:
                print("Tenant not found.")

        elif choice == '16':
            # View properties owned by a specific owner
            try:
                owner_id = int(input("Enter owner ID to view properties: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for owner ID.")
                continue  # Restart the loop to prompt the user again

            properties = Property.get_properties_by_owner(owner_id)
            if properties:
                print(f"Properties owned by Owner ID {owner_id}:")
                for property in properties:
                    print(f"ID: {property[0]}, Address: {property[1]}")
            else:
                print("No properties found for this owner.")

            # View tenants residing in a particular property
            try:
                property_id = int(input("Enter property ID to view tenants: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for property ID.")
                continue  # Restart the loop to prompt the user again

            tenants = Tenant.get_tenants_by_property(property_id)
            if tenants:
                print(f"Tenants residing in Property ID {property_id}:")
                for tenant in tenants:
                    print(f"ID: {tenant[0]}, Name: {tenant[1]}")
            else:
                print("No tenants found for this property.")

        elif choice == '17':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()