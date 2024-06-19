import sqlite3
import sys

def insert_sample_data(tenant_id, user_id, username, email, password, full_name, address, phone_number, project_id, project_name, task_id, task_name, task_status, comment_id, comment_text, permission_id, permission_type, setting_id, setting_name, setting_value):
    connection = sqlite3.connect(f'{tenant_id}.db')
    cursor = connection.cursor()

    # Insert into Users
    cursor.execute("INSERT INTO Users (user_id, username, email, password) VALUES (?, ?, ?, ?);", 
                   (user_id, username, email, password))

    # Insert into Permissions
    cursor.execute("INSERT INTO Permissions (permission_id, user_id, permission_type) VALUES (?, ?, ?);", 
                   (permission_id, user_id, permission_type))

    # Insert into PersonalDetails
    cursor.execute("INSERT INTO PersonalDetails (user_id, full_name, address, phone_number) VALUES (?, ?, ?, ?);", 
                   (user_id, full_name, address, phone_number))

    # Insert into Settings
    cursor.execute("INSERT INTO Settings (setting_id, user_id, setting_name, setting_value) VALUES (?, ?, ?, ?);", 
                   (setting_id, user_id, setting_name, setting_value))

    # Insert into Projects
    cursor.execute("INSERT INTO Projects (project_id, user_id, project_name) VALUES (?, ?, ?);", 
                   (project_id, user_id, project_name))

    # Insert into Tasks
    cursor.execute("INSERT INTO Tasks (task_id, project_id, task_name, status) VALUES (?, ?, ?, ?);", 
                   (task_id, project_id, task_name, task_status))

    # Insert into Comments
    cursor.execute("INSERT INTO Comments (comment_id, task_id, comment_text) VALUES (?, ?, ?);", 
                   (comment_id, task_id, comment_text))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 21:  # Update the expected argument count to 21
        print("Usage: python insert_sample_data_tenant.py <tenant_id> <user_id> <username> <email> <password> <full_name> <address> <phone_number> <project_id> <project_name> <task_id> <task_name> <task_status> <comment_id> <comment_text> <permission_id> <permission_type> <setting_id> <setting_name> <setting_value>")
    else:
        tenant_id = int(sys.argv[1])
        user_id = int(sys.argv[2])
        username = sys.argv[3]
        email = sys.argv[4]
        password = sys.argv[5]
        full_name = sys.argv[6]
        address = sys.argv[7]
        phone_number = sys.argv[8]
        project_id = int(sys.argv[9])
        project_name = sys.argv[10]
        task_id = int(sys.argv[11])
        task_name = sys.argv[12]
        task_status = sys.argv[13]
        comment_id = int(sys.argv[14])
        comment_text = sys.argv[15]
        permission_id = int(sys.argv[16])
        permission_type = sys.argv[17]
        setting_id = int(sys.argv[18])
        setting_name = sys.argv[19]
        setting_value = sys.argv[20]
        insert_sample_data(tenant_id, user_id, username, email, password, full_name, address, phone_number, project_id, project_name, task_id, task_name, task_status, comment_id, comment_text, permission_id, permission_type, setting_id, setting_name, setting_value)
        print(f"Inserted sample data into tenant database {tenant_id}.db")

