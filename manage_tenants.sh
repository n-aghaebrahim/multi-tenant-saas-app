#!/bin/bash

# Function to run unit tests
run_tests() {
    echo "Running tests..."
    PYTHONPATH=./scripts:./src pytest tests/
}

# Function to create a tenant database
create_tenant() {
    if [ -z "$1" ]; then
        echo "Tenant ID not provided. Usage: $0 create_tenant <tenant_id>"
        exit 1
    fi
    PYTHONPATH=./scripts python scripts/create_tenant_database.py $1
    echo "Created tenant database for tenant ID: $1"
}

# Function to create the shared database schema
create_shared_database() {
    PYTHONPATH=./scripts python scripts/create_shared_database.py
}

# Function to remove a tenant database
remove_tenant() {
    if [ -z "$1" ]; then
        echo "Tenant ID not provided. Usage: $0 remove_tenant <tenant_id>"
        exit 1
    fi
    rm -f "$1.db"
    echo "Removed tenant database for tenant ID: $1"
}

# Function to retrieve information from a tenant database
retrieve_information() {
    if [ -z "$1" ]; then
        echo "Tenant ID not provided. Usage: $0 retrieve_information <tenant_id>"
        exit 1
    fi
    if [ ! -f "$1.db" ]; then
        echo "Database for tenant ID: $1 does not exist."
        exit 1
    fi
    echo "Retrieving Users..."
    sqlite3 "$1.db" "SELECT * FROM Users;" | while read -r row; do
        echo "$row"
    done

    echo "Retrieving Projects..."
    sqlite3 "$1.db" "SELECT * FROM Projects;" | while read -r row; do
        echo "$row"
    done

    echo "Retrieving Tasks..."
    sqlite3 "$1.db" "SELECT * FROM Tasks;" | while read -r row; do
        echo "$row"
    done

    echo "Retrieving Comments..."
    sqlite3 "$1.db" "SELECT * FROM Comments;" | while read -r row; do
        echo "$row"
    done

    echo "Retrieving Permissions..."
    sqlite3 "$1.db" "SELECT * FROM Permissions;" | while read -r row; do
        echo "$row"
    done
}

# Function to insert sample data into the shared database
insert_sample_data_shared() {
    PYTHONPATH=./scripts python scripts/insert_sample_data_shared.py
}

# Main script logic
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 {run_tests|create_tenant|create_shared_database|remove_tenant|retrieve_information|insert_sample_data_shared} [args]"
    exit 1
fi

command=$1
shift

case "$command" in
    run_tests)
        run_tests
        ;;
    create_tenant)
        create_tenant "$@"
        ;;
    create_shared_database)
        create_shared_database
        ;;
    remove_tenant)
        remove_tenant "$@"
        ;;
    retrieve_information)
        retrieve_information "$@"
        ;;
    insert_sample_data_shared)
        insert_sample_data_shared
        ;;
    *)
        echo "Unknown command: $command"
        echo "Usage: $0 {run_tests|create_tenant|create_shared_database|remove_tenant|retrieve_information|insert_sample_data_shared} [args]"
        exit 1
        ;;
esac

