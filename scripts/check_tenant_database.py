import sqlite3
import sys

def check_tenant_database(tenant_id):
    connection = sqlite3.connect(f'{tenant_id}.db')
    cursor = connection.cursor()

    # Retrieve all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print(f"Tables in {tenant_id}.db: {tables}")

    for table in tables:
        table_name = table[0]
        print(f"Schema for table {table_name}:")
        cursor.execute(f"PRAGMA table_info({table_name});")
        schema = cursor.fetchall()
        for column in schema:
            print(column)

        print(f"Data in table {table_name}:")
        cursor.execute(f"SELECT * FROM {table_name};")
        data = cursor.fetchall()
        for row in data:
            print(row)

    connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_tenant_database.py <tenant_id>")
    else:
        tenant_id = int(sys.argv[1])
        check_tenant_database(tenant_id)

