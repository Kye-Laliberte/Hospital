import sqlite3
import os

def initialize_database(db_path="app.db", schema_path="SQL/Medical_data.sql"):
    """
    Creates or updates the SQLite database using the provided schema file.
    If tables already exist, they won't be recreated.
    """
    
    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"Schema file not found: {schema_path}")

    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        with open(schema_path, "r", encoding="utf-8") as file:
            schema_sql = file.read()

        cursor.executescript(schema_sql)
        conn.commit()
        print("Database setup completed successfully.")

    except sqlite3.Error as e:
        print(f"SQLite error during setup: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        conn.close()