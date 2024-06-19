import sqlite3

def create_tenant_database(tenant_id):
    connection = sqlite3.connect(f'{tenant_id}.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Permissions (
        permission_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        permission_type TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PersonalDetails (
        detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        full_name TEXT,
        address TEXT,
        phone_number TEXT,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Settings (
        setting_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        setting_name TEXT NOT NULL,
        setting_value TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Projects (
        project_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        project_name TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        task_name TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (project_id) REFERENCES Projects(project_id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Comments (
        comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id INTEGER,
        comment_text TEXT NOT NULL,
        FOREIGN KEY (task_id) REFERENCES Tasks(task_id)
    );
    ''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python create_tenant_database.py <tenant_id>")
    else:
        create_tenant_database(sys.argv[1])
        print(f"Created tenant database for tenant ID: {sys.argv[1]}")

