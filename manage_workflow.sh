#!/bin/bash

# Function to create a tenant database
create_tenant() {
    tenant_id=$1
    ./manage_tenants.sh create_tenant "$tenant_id"
}

# Function to insert sample data into a tenant database
insert_sample_data_tenant() {
    tenant_id=$1
    user_id=$2
    username=$3
    email=$4
    password=$5
    full_name=$6
    address=$7
    phone_number=$8
    project_id=$9
    project_name=${10}
    task_id=${11}
    task_name=${12}
    task_status=${13}
    comment_id=${14}
    comment_text=${15}
    permission_id=${16}
    permission_type=${17}
    setting_id=${18}
    setting_name=${19}
    setting_value=${20}
    PYTHONPATH=./scripts python scripts/insert_sample_data_tenant.py "$tenant_id" "$user_id" "$username" "$email" "$password" "$full_name" "$address" "$phone_number" "$project_id" "$project_name" "$task_id" "$task_name" "$task_status" "$comment_id" "$comment_text" "$permission_id" "$permission_type" "$setting_id" "$setting_name" "$setting_value"
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

# Function to check the tenant database
check_tenant_database() {
    tenant_id=$1
    PYTHONPATH=./scripts python scripts/check_tenant_database.py "$tenant_id"
}

# Main workflow
main() {
    tenant_id=123
    user_id=1
    username="user123"
    email="user123@example.com"
    password="password123"
    full_name="User One Two Three"
    address="123 Main St"
    phone_number="555-0123"
    project_id=1
    project_name="Project123"
    task_id=1
    task_name="Task123"
    task_status="Pending"
    comment_id=1
    comment_text="This is a comment."
    permission_id=1
    permission_type="read"
    setting_id=1
    setting_name="theme"
    setting_value="dark"

    echo "Creating tenant database..."
    create_tenant "$tenant_id"
    
    echo "Inserting sample data into tenant database..."
    insert_sample_data_tenant "$tenant_id" "$user_id" "$username" "$email" "$password" "$full_name" "$address" "$phone_number" "$project_id" "$project_name" "$task_id" "$task_name" "$task_status" "$comment_id" "$comment_text" "$permission_id" "$permission_type" "$setting_id" "$setting_name" "$setting_value"
    
    echo "Creating shared database schema..."
    create_shared_database
    
    echo "Inserting sample data into shared database..."
    insert_sample_data_shared
    
    echo "Retrieving information from tenant database..."
    retrieve_information "$tenant_id"
    
    echo "Checking tenant database..."
    check_tenant_database "$tenant_id"
    
    echo "Checking shared database..."
    check_shared_database
    
    echo "Workflow completed successfully."
}

# Execute the main workflow
main

