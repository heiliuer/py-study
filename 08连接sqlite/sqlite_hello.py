import sqlite3
import uuid
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
for i in range(10):
    cursor.execute('INSERT INTO user (id, name) VALUES (\'' + str(uuid.uuid1()) + '\', \'Michael\')')
cursor.close()
conn.commit()
