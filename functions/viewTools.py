import sqlite3

def viewTable(table_name, db_path="app.db", limit=20):
    """
    Prints the first `limit` rows of a table for quick inspection.
    Catches errors if the table does not exist.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Use a safe query to check if the table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table_name,))
        if not cursor.fetchone():
            print(f"Table '{table_name}' does not exist in the database.")
            return
        
        cursor.execute(f"SELECT * FROM {table_name} LIMIT {limit};")
        rows = cursor.fetchall()
        
        if not rows:
            print(f"No data found in table '{table_name}'.")
            return
        
        # Print column headers
        col_names = [description[0] for description in cursor.description]
        print(" | ".join(col_names))
        print("-" * 50)
        
        # Print rows
        for row in rows:
            print(" | ".join(str(r) for r in row))
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()