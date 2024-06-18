import sqlite3

def check_shared_database():
    connection = sqlite3.connect('shared_tenant.db')
    cursor = connection.cursor()

    tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    print("Tables in shared_tenant.db:", tables)

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
    check_shared_database()

