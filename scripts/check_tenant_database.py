import sqlite3

def check_tenant_database(tenant_id):
    connection = sqlite3.connect(f'{tenant_id}.db')
    cursor = connection.cursor()

    tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    print(f"Tables in tenant database {tenant_id}.db: {tables}")

    for table in tables:
        print(f"Schema for table {table[0]}:")
        schema = cursor.execute(f"PRAGMA table_info({table[0]});").fetchall()
        for column in schema:
            print(column)
        print("\nData in table", table[0], ":")
        data = cursor.execute(f"SELECT * FROM {table[0]};").fetchall()
        for row in data:
            print(row)
        print("\n")

    connection.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python check_tenant_database.py <tenant_id>")
    else:
        check_tenant_database(sys.argv[1])

