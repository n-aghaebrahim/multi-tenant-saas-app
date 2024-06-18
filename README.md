# Multi-Tenant Database Project

This project demonstrates how to create a multi-tenant SQLite database with both "Database Per Tenant" and "Shared Database, Isolated Schemas" strategies. The project includes scripts to create and manage tenant databases, insert sample data, and retrieve information from these databases.

## Project Structure

multi-tenant-database/
├── .gitignore
├── README.md
├── LICENSE
├── requirements.txt
├── manage_tenants.sh
├── scripts/
│ ├── create_tenant_database.py
│ ├── create_shared_database.py
│ ├── insert_sample_data.py
│ ├── insert_sample_data_shared.py
│ ├── connection_manager.py
│ ├── check_tenant_database.py
│ ├── check_shared_database.py
├── src/
│ ├── init.py
│ ├── models.py
│ ├── queries.py
├── tests/
│ ├── init.py
│ ├── test_create_tenant_database.py
│ ├── test_create_shared_database.py
│ ├── test_queries.py
└── config/
└── settings.py



## Setup

### Prerequisites

- Python 3.7 or later
- `pip` (Python package installer)
- `sqlite3` (SQLite command-line tool)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/multi-tenant-database.git
   cd multi-tenant-database

2. **Create a virtual environment and activate it**:
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt


Usage

Manage Tenants Script
The manage_tenants.sh script provides various commands to manage the tenant databases.


Commands

Run unit tests:

```bash
./manage_tenants.sh run_tests
Create a tenant database:

```bash
./manage_tenants.sh create_tenant <tenant_id>
Create the shared database schema:

```bash
./manage_tenants.sh create_shared_database
Insert sample data into the shared database:

```bash
./manage_tenants.sh insert_sample_data_shared
Remove a tenant database:

```bash
./manage_tenants.sh remove_tenant <tenant_id>
Retrieve information from a tenant database:

```bash
./manage_tenants.sh retrieve_information <tenant_id>
Example Workflow
Create a tenant database:

```bash
./manage_tenants.sh create_tenant 1
Insert sample data into a tenant database:

```bash
PYTHONPATH=./scripts python scripts/insert_sample_data.py
Create the shared database schema:

```bash
./manage_tenants.sh create_shared_database
Insert sample data into the shared database:

```bash
./manage_tenants.sh insert_sample_data_shared
Retrieve information from a tenant database:

```bash
./manage_tenants.sh retrieve_information 1
Check the shared database:

```bash
PYTHONPATH=./scripts python scripts/check_shared_database.py



Directory Details

scripts/: Contains scripts for creating databases, inserting sample data, and checking database contents.

create_tenant_database.py: Creates a separate database for each tenant.
create_shared_database.py: Creates a shared database with isolated schemas for tenants.
insert_sample_data.py: Inserts sample data into a tenant database.
insert_sample_data_shared.py: Inserts sample data into the shared database.
check_tenant_database.py: Checks the contents of a tenant database.
check_shared_database.py: Checks the contents of the shared database.
src/: Contains the main application code.

models.py: Defines the database schema and models using SQLAlchemy.
queries.py: Contains functions for executing database queries.
tests/: Contains unit tests for the project.

test_create_tenant_database.py: Unit tests for tenant database creation.
test_create_shared_database.py: Unit tests for shared database creation.
test_queries.py: Unit tests for query functions.
config/: Contains configuration files.

settings.py: Configuration settings for the project.


