import sqlite3

def insert_sample_data(tenant_id):
    connection = sqlite3.connect(f'{tenant_id}.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Users (tenant_id, username, email, password) VALUES (?, ?, ?, ?);", 
                   (tenant_id, 'user1', 'user1@example.com', 'password123'))

    cursor.execute("INSERT INTO Projects (tenant_id, user_id, project_name) VALUES (?, ?, ?);", 
                   (tenant_id, 1, 'Project1'))

    cursor.execute("INSERT INTO Tasks (tenant_id, project_id, task_name, status) VALUES (?, ?, ?, ?);", 
                   (tenant_id, 1, 'Task1', 'Pending'))

    cursor.execute("INSERT INTO Comments (tenant_id, task_id, comment_text) VALUES (?, ?, ?);", 
                   (tenant_id, 1, 'This is a comment.'))

    cursor.execute("INSERT INTO Permissions (tenant_id, user_id, permission_type) VALUES (?, ?, ?);", 
                   (tenant_id, 1, 'read'))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    tenant_id = 1  # Change as needed
    insert_sample_data(tenant_id)
    print(f"Inserted sample data into tenant database {tenant_id}.db")

