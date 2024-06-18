#!/bin/bash

# Function to create a tenant database
create_tenant() {
    tenant_id=$1
    ./manage_tenants.sh create_tenant "$tenant_id"
}

# Function to insert sample data into a tenant database
insert_sample_data_tenant() {
    tenant_id=$1
    PYTHONPATH=./scripts python scripts/insert_sample_data_tenant.py "$tenant_id"
}

# Function to create the shared database schema
create_shared_database() {
    ./manage_tenants.sh create_shared_database
}

# Function to insert sample data into the shared database
insert_sample_data_shared() {
    ./manage_tenants.sh insert_sample_data_shared
}

# Function to retrieve information from a tenant database
retrieve_information() {
    tenant_id=$1
    ./manage_tenants.sh retrieve_information "$tenant_id"
}

# Function to check the shared database
check_shared_database() {
    PYTHONPATH=./scripts python scripts/check_shared_database.py
}

# Main workflow
main() {
    #tenant_id=1
	database_name='test1'

    echo "Creating tenant database..."
    create_tenant "$database_name"
    
    echo "Inserting sample data into tenant database..."
    insert_sample_data_tenant "$database_name"
    
    echo "Creating shared database schema..."
    create_shared_database
    
    echo "Inserting sample data into shared database..."
    insert_sample_data_shared
    
    echo "Retrieving information from tenant database..."
    retrieve_information "$database_name"
    
    echo "Checking shared database..."
    check_shared_database
    
    echo "Workflow completed successfully."
}

# Execute the main workflow
main

