from models import Owner, Property, Tenant

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
            name = input("Enter owner's name: ")
            phone_number = input("Enter owner's phone number: ")
            physical_address = input("Enter owner's physical address: ")
            occupation = input("Enter owner's occupation: ")
            Owner.create(name, phone_number, physical_address, occupation)

        elif choice == '2':
            owner_id = int(input("Enter owner ID to update: "))
            owner = Owner.find_by_id(owner_id)
            if owner:
                name = input(f"Enter new name for owner ({owner[1]}): ")
                phone_number = input(f"Enter new phone number for owner ({owner[2]}): ")
                physical_address = input(f"Enter new physical address for owner ({owner[3]}): ")
                occupation = input(f"Enter new occupation for owner ({owner[4]}): ")
                Owner.update(owner_id, name, phone_number, physical_address, occupation)
            else:
                print("Owner not found.")

        elif choice == '3':
            owner_id = int(input("Enter owner ID to delete: "))
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
            owner_id = int(input("Enter owner ID to find: "))
            owner = Owner.find_by_id(owner_id)
            if owner:
                print(f"Owner ID: {owner[0]}, Name: {owner[1]}")
            else:
                print("Owner not found.")         

            # Property Methods
        elif choice == '6':
            address = input("Enter property address: ")
            owner_id = int(input("Enter owner ID for this property: "))
            Property.create(address, owner_id)

        elif choice == '7':
            property_id = int(input("Enter property ID to update: "))
            property = Property.find_by_id(property_id)
            if property:
                address = input(f"Enter new address for property ({property[1]}): ")
                Property.update(property_id, address)
            else:
                print("Property not found.")

        elif choice == '8':
            property_id = int(input("Enter property ID to delete: "))
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
            property_id = int(input("Enter property ID to find: "))
            property = Property.find_by_id(property_id)
            if property:
                print(f"Property ID: {property[0]}, Address: {property[1]}, Owner ID: {property[2]}")
            else:
                print("Property not found.")


            # Tenant Methods
        elif choice == '11':
            name = input("Enter tenant's name: ")
            phone_number = input("Enter tenant's phone number: ")
            physical_address = input("Enter tenant's physical address: ")
            property_id = int(input("Enter property ID for this tenant: "))
            Tenant.create(name, phone_number, physical_address, property_id)

        elif choice == '12':
            tenant_id = int(input("Enter tenant ID to update: "))
            tenant = Tenant.find_by_id(tenant_id)
            if tenant:
                name = input(f"Enter new name for tenant ({tenant[1]}): ")
                phone_number = input(f"Enter new phone number for tenant ({tenant[2]}): ")
                physical_address = input(f"Enter new physical address for tenant ({tenant[3]}): ")
                Tenant.update(tenant_id, name, phone_number, physical_address)
            else:
                print("Tenant not found.")

        elif choice == '13':
            tenant_id = int(input("Enter tenant ID to delete: "))
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
            tenant_id = int(input("Enter tenant ID to find: "))
            tenant = Tenant.find_by_id(tenant_id)
            if tenant:
                print(f"Tenant ID: {tenant[0]}, Name: {tenant[1]}, Property ID: {tenant[4]}")
            else:
                print("Tenant not found.")

        elif choice == '16':
            # View properties owned by a specific owner
            owner_id = int(input("Enter owner ID to view properties: "))
            properties = Property.get_properties_by_owner(owner_id)
            if properties:
                print(f"Properties owned by Owner ID {owner_id}:")
                for property in properties:
                    print(f"ID: {property[0]}, Address: {property[1]}")
            else:
                print("No properties found for this owner.")

            # View tenants residing in a particular property
            property_id = int(input("Enter property ID to view tenants: "))
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