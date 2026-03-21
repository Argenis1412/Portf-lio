import sqlite3
import os

db_path = 'backend/portfolio.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"Tables: {tables}")
    for table in tables:
        t_name = table[0]
        cursor.execute(f"PRAGMA table_info({t_name})")
        print(f"\nTable {t_name}:")
        for col in cursor.fetchall():
            print(f"  {col}")
    conn.close()
else:
    print(f"File {db_path} not found.")
