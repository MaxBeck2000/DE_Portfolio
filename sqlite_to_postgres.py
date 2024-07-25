import sqlite3
import psycopg2
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import time

dbname="nhai"
user="postgres"
password=""
host="localhost"
port=5432  

# Paths and connection details
sqlite_db_path = r'C:\Users\suici\Github\Indian_Tolls_Scrape\nhai_info.db'
postgres_connection_string = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

# Function to create table in PostgreSQL with quoted identifiers
def create_postgres_table(postgres_conn, table_name, columns):
    create_table_stmt = f'CREATE TABLE IF NOT EXISTS "{table_name}" ('
    for col in columns:
        col_name = col[1]
        col_type = col[2].upper()  # Convert SQLite type to uppercase to match PostgreSQL types
        create_table_stmt += f'"{col_name}" {col_type}, '
    create_table_stmt = create_table_stmt.rstrip(", ") + ");"
    
    try:
        with postgres_conn.cursor() as cursor:
            cursor.execute(create_table_stmt)
            postgres_conn.commit()
    except SQLAlchemyError as e:
        print(f"Error creating table {table_name}: {e}")
        postgres_conn.rollback()

# Function to insert data in batches
def insert_data_in_batches(postgres_conn, table_name, rows, batch_size=1000):
    for i in range(0, len(rows), batch_size):
        batch = rows[i:i + batch_size]
        if not batch:
            continue
        
        # Dynamically create the INSERT statement with placeholders
        placeholders = ', '.join(['%s'] * len(batch[0]))
        insert_stmt = f'INSERT INTO "{table_name}" VALUES ({placeholders})'
        
        try:
            with postgres_conn.cursor() as cursor:
                cursor.executemany(insert_stmt, batch)
                postgres_conn.commit()
        except SQLAlchemyError as e:
            print(f"Error inserting data into table {table_name}: {e}")
            postgres_conn.rollback()

# Main script
try:
    # Connect to SQLite
    sqlite_conn = sqlite3.connect(sqlite_db_path)
    sqlite_cursor = sqlite_conn.cursor()

    # Connect to PostgreSQL
    postgres_engine = create_engine(postgres_connection_string)
    postgres_conn = postgres_engine.raw_connection()

    # Get SQLite table names
    sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = sqlite_cursor.fetchall()

    # Process each table
    for table_name in tables:
        table_name = table_name[0]
        print(f"Processing table {table_name}...")
        start_time = time.time()

        # Get table schema from SQLite
        sqlite_cursor.execute(f"PRAGMA table_info('{table_name}');")
        columns = sqlite_cursor.fetchall()
        create_postgres_table(postgres_conn, table_name, columns)

        # Copy data from SQLite to PostgreSQL
        sqlite_cursor.execute(f"SELECT * FROM '{table_name}'")
        rows = sqlite_cursor.fetchall()
        if rows:
            insert_data_in_batches(postgres_conn, table_name, rows)

        end_time = time.time()
        print(f"Finished processing table {table_name} in {end_time - start_time} seconds.")

    # Close connections
    sqlite_conn.close()
    postgres_conn.close()

    print("Migration completed successfully!")

except Exception as e:
    print(f"Error during migration: {e}")
