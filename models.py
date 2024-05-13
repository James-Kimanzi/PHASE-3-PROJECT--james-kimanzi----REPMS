import sqlite3

# Create a SQLite database
conn = sqlite3.connect('property_management.db')
cursor = conn.cursor()

# Function to create tables if they don't exist
def create_tables_if_not_exist():
    # Connect to the SQLite database
    conn = sqlite3.connect('property_management.db')
    cursor = conn.cursor()

    # Check if tables exist by querying the SQLite master table
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='owners';")
    owners_table_exists = cursor.fetchone() is not None

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='properties';")
    properties_table_exists = cursor.fetchone() is not None

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tenants';")
    tenants_table_exists = cursor.fetchone() is not None

    # Create tables if they don't exist
    if not owners_table_exists:
        cursor.execute('''CREATE TABLE owners (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            phone_number TEXT,
                            physical_address TEXT,
                            occupation TEXT
                        );''')

    if not properties_table_exists:
        cursor.execute('''CREATE TABLE properties (
                            id INTEGER PRIMARY KEY,
                            address TEXT NOT NULL,
                            owner_id INTEGER,
                            FOREIGN KEY (owner_id) REFERENCES owners (id)
                        );''')

    if not tenants_table_exists:
        cursor.execute('''CREATE TABLE tenants (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            phone_number TEXT,
                            physical_address TEXT,
                            property_id INTEGER,
                            FOREIGN KEY (property_id) REFERENCES properties (id)
                        );''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Call the function to create tables if they don't exist
if __name__ == "__main__":
    create_tables_if_not_exist()

# Define the Owner class with ORM methods
class Owner:
    def __init__(self, name, phone_number=None, physical_address=None, occupation=None):
        self.name = name
        self.phone_number = phone_number
        self.physical_address = physical_address
        self.occupation = occupation

    @staticmethod
    def create(name, phone_number=None, physical_address=None, occupation=None):
        cursor.execute(
            'INSERT INTO owners (name, phone_number, physical_address, occupation) VALUES (?, ?, ?, ?)',
            (name, phone_number, physical_address, occupation)
        )
        conn.commit()

    @staticmethod
    def update(owner_id, name, phone_number=None, physical_address=None, occupation=None):
        cursor.execute(
            'UPDATE owners SET name=?, phone_number=?, physical_address=?, occupation=? WHERE id=?',
            (name, phone_number, physical_address, occupation, owner_id)
        )
        conn.commit()

    @staticmethod
    def delete(owner_id):
        confirmation = input("Are you sure you want to delete this owner? (y/n): ")
        if confirmation.lower() == 'y':
            cursor.execute('DELETE FROM owners WHERE id=?', (owner_id,))
            conn.commit()

    @staticmethod
    def get_all():
        cursor.execute('SELECT * FROM owners')
        return cursor.fetchall()

    @staticmethod
    def find_by_id(owner_id):
        cursor.execute('SELECT * FROM owners WHERE id=?', (owner_id,))
        return cursor.fetchone()

# Define the Property class with ORM methods
class Property:
    def __init__(self, address, owner_id=None):
        self.address = address
        self.owner_id = owner_id

    @staticmethod
    def create(address, owner_id=None):
        cursor.execute('INSERT INTO properties (address, owner_id) VALUES (?, ?)', (address, owner_id))
        conn.commit()

    @staticmethod
    def update(property_id, address):
        cursor.execute('UPDATE properties SET address=? WHERE id=?', (address, property_id))
        conn.commit()

    @staticmethod
    def delete(property_id):
        confirmation = input("Are you sure you want to delete this property? (y/n): ")
        if confirmation.lower() == 'y':
            cursor.execute('DELETE FROM properties WHERE id=?', (property_id,))
            conn.commit()

    @staticmethod
    def get_all():
        cursor.execute('SELECT * FROM properties')
        return cursor.fetchall()

    @staticmethod
    def find_by_id(property_id):
        cursor.execute('SELECT * FROM properties WHERE id=?', (property_id,))
        return cursor.fetchone()
    
    @staticmethod
    def get_properties_by_owner(owner_id):
        cursor.execute('SELECT * FROM properties WHERE owner_id=?', (owner_id,))
        return cursor.fetchall()

# Define the Tenant class with ORM methods
class Tenant:
    def __init__(self, name, phone_number=None, physical_address=None, property_id=None):
        self.name = name
        self.phone_number = phone_number
        self.physical_address = physical_address
        self.property_id = property_id

    @staticmethod
    def create(name, phone_number=None, physical_address=None, property_id=None):
        cursor.execute(
            'INSERT INTO tenants (name, phone_number, physical_address, property_id) VALUES (?, ?, ?, ?)',
            (name, phone_number, physical_address, property_id)
        )
        conn.commit()

    @staticmethod
    def update(tenant_id, name, phone_number=None, physical_address=None):
        cursor.execute(
            'UPDATE tenants SET name=?, phone_number=?, physical_address=? WHERE id=?',
            (name, phone_number, physical_address, tenant_id)
        )
        conn.commit()

    @staticmethod
    def delete(tenant_id):
        confirmation = input("Are you sure you want to delete this tenant? (y/n): ")
        if confirmation.lower() == 'y':
            cursor.execute('DELETE FROM tenants WHERE id=?', (tenant_id,))
            conn.commit()

    @staticmethod
    def get_all():
        cursor.execute('SELECT * FROM tenants')
        return cursor.fetchall()

    @staticmethod
    def find_by_id(tenant_id):
        cursor.execute('SELECT * FROM tenants WHERE id=?', (tenant_id,))
        return cursor.fetchone()
    
    @staticmethod
    def get_tenants_by_property(property_id):
        cursor.execute('SELECT * FROM tenants WHERE property_id=?', (property_id,))
        return cursor.fetchall()
