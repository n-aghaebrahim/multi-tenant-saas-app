import sqlite3

def insert_sample_data_shared(tenant_id):
    connection = sqlite3.connect('shared_tenant.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Users (tenant_id, username, email, password) VALUES (?, ?, ?, ?);", 
                   (tenant_id, f'user{tenant_id}', f'user{tenant_id}@example.com', 'password123'))

    cursor.execute("INSERT INTO Projects (tenant_id, user_id, project_name) VALUES (?, (SELECT user_id FROM Users WHERE tenant_id=?), ?);", 
                   (tenant_id, tenant_id, f'Project{tenant_id}'))

    cursor.execute("INSERT INTO Tasks (tenant_id, project_id, task_name, status) VALUES (?, (SELECT project_id FROM Projects WHERE tenant_id=?), ?, ?);", 
                   (tenant_id, tenant_id, f'Task{tenant_id}', 'Pending'))

    cursor.execute("INSERT INTO Comments (tenant_id, task_id, comment_text) VALUES (?, (SELECT task_id FROM Tasks WHERE tenant_id=?), ?);", 
                   (tenant_id, tenant_id, f'This is a comment from tenant {tenant_id}.'))

    cursor.execute("INSERT INTO Permissions (tenant_id, user_id, permission_type) VALUES (?, (SELECT user_id FROM Users WHERE tenant_id=?), ?);", 
                   (tenant_id, tenant_id, 'read'))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    tenant_ids = [1, 2]  # Change as needed to insert data for multiple tenants
    for tenant_id in tenant_ids:
        insert_sample_data_shared(tenant_id)
        print(f"Inserted sample data for tenant ID {tenant_id} into shared_tenant.db")

