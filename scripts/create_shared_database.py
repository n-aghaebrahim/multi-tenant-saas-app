import sqlite3

def create_shared_database():
    connection = sqlite3.connect('shared_tenant.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tenant_id INTEGER,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        UNIQUE(tenant_id, email)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Projects (
        project_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tenant_id INTEGER,
        user_id INTEGER,
        project_name TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id),
        UNIQUE(tenant_id, project_name)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tenant_id INTEGER,
        project_id INTEGER,
        task_name TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (project_id) REFERENCES Projects(project_id),
        UNIQUE(tenant_id, task_name)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Comments (
        comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tenant_id INTEGER,
        task_id INTEGER,
        comment_text TEXT NOT NULL,
        FOREIGN KEY (task_id) REFERENCES Tasks(task_id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Permissions (
        permission_id INTEGER PRIMARY KEY AUTOINCREMENT,
        tenant_id INTEGER,
        user_id INTEGER,
        permission_type TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    ''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_shared_database()
    print("Created shared database schema")

