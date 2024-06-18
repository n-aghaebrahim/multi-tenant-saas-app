import sqlite3

def get_connection(tenant_id, strategy='database_per_tenant'):
    if strategy == 'database_per_tenant':
        return sqlite3.connect(f'{tenant_id}.db')
    elif strategy == 'shared_database':
        return sqlite3.connect('shared_tenant.db')
    else:
        raise ValueError("Unsupported strategy")

# Example usage
if __name__ == "__main__":
    tenant_id = 1
    strategy = 'database_per_tenant'
    connection = get_connection(tenant_id, strategy)
    cursor = connection.cursor()

    # Example query
    cursor.execute('SELECT * FROM Users WHERE tenant_id = ?', (tenant_id,))
    users = cursor.fetchall()
    print(users)

    connection.close()

