import psycopg2
from sqlalchemy import create_engine, text

# PostgreSQL database connection details
postgres_connection_string = 'postgresql://postgres:***REMOVED***@localhost:5432/nhai'

try:
    # Using psycopg2 directly
    conn = psycopg2.connect(
        dbname="nhai",       # Name of the database
        user="postgres",     # Username
        password="***REMOVED***",   # Password
        host="localhost",    # Host
        port=5432            # Port (must be an integer)
    )
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("Connected to PostgreSQL database!")
    print(f"Database version: {db_version[0]}")
    cursor.close()
    conn.close()

    # Using SQLAlchemy
    engine = create_engine(postgres_connection_string)
    with engine.connect() as connection:
        # Use text() to execute raw SQL queries
        result = connection.execute(text("SELECT version();"))
        for row in result:
            print(f"Database version (SQLAlchemy): {row[0]}")
    
    print("SQLAlchemy connection successful!")

except Exception as e:
    print(f"Error connecting to PostgreSQL: {e}")
