import sqlite3

def create_tenant_database(tenant_id):
    connection = sqlite3.connect(f'{tenant_id}.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tenant_id INTEGER,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE Projects (
        project_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tenant_id INTEGER,
        user_id INTEGER,
        project_name TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE Tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tenant_id INTEGER,
        project_id INTEGER,
        task_name TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (project_id) REFERENCES Projects(project_id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE Comments (
        comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tenant_id INTEGER,
        task_id INTEGER,
        comment_text TEXT NOT NULL,
        FOREIGN KEY (task_id) REFERENCES Tasks(task_id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE Permissions (
        permission_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tenant_id INTEGER,
        user_id INTEGER,
        permission_type TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    ''')

    connection.commit()
    connection.close()

# Example: Create databases for tenants 1 and 2
if __name__ == "__main__":
    create_tenant_database(1)
    create_tenant_database(2)

