import sqlite3

DATABASE_NAME = "inventory.db"


def get_connection():
    """Return a connection to the local inventory database."""
    pass


def initialize_database(connection):
    """Create the products table and add sample data when it is empty."""
    pass


def add_product(connection, name, category, quantity, price):
    """Insert a product and return its new identifier."""
    pass


def list_products(connection):
    """Return all products ordered by name."""
    pass


def search_products(connection, search_term):
    """Return products whose name or category matches the search term."""
    pass


def update_quantity(connection, product_id, quantity):
    """Update a product quantity and return whether a row was changed."""
    pass


def delete_product(connection, product_id):
    """Delete a product and return whether a row was deleted."""
    pass


def inventory_report(connection):
    """Return the total inventory value and products needing restock."""
    pass


def run_menu(connection):
    """Run the command-line inventory menu until the user exits."""
    pass


def main():
    connection = get_connection()
    try:
        initialize_database(connection)
        run_menu(connection)
    finally:
        connection.close()


if __name__ == "__main__":
    main()
