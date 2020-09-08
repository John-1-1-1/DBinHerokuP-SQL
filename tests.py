import os
import psycopg2

db = os.environ['DATABASE_URL']

conn = psycopg2.connect(db, sslmode='require')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE STUDENT  
     (ADMISSION INT PRIMARY KEY NOT NULL,
     NAME TEXT NOT NULL,
     AGE INT NOT NULL,
     COURSE CHAR(50),
     DEPARTMENT CHAR(50));''')
cursor.execute('''INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT)
VALUES (3420, 'John', 18, 'Computer Science', 'ICT')
''')
conn.commit() 
cursor.close()
conn.close()
