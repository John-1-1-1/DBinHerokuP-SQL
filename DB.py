from operator import itemgetter
import psycopg2
import data
import os


class DB(object):
    def __init__(self):
        self.conn = ""
        try:
            import password_data
            self.conn = psycopg2.connect(dbname=password_data.dbname,
                                    user=password_data.user,
                                    password=password_data.password,
                                    host=password_data.host)
        except ImportError:
            db = os.environ['DATABASE_URL']
            self.conn = psycopg2.connect(db, sslmode='require')

    def CreateDB(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS {0} (
              id INTEGER PRIMARY KEY,
              DataTime TEXT,
              Temperature1 INTEGER,
              Temperamure2 INTEGER,
              Humidity INTEGER
            );
            """.format(data.name_db))
        self.conn.commit()
        cursor.close()

    def execut_query(self, request):
        cursor = self.conn.cursor()
        cursor.execute(request)
        return cursor

    def GetCommits(self):
        select_users = "SELECT * from {0}".format(data.name_db)
        users =sorted(
            self.execut_query(select_users)\
                .fetchall(),
            key=itemgetter(0))
        return users

    def SetCommits(self,id,DataTime, temp1, temp2, hum):
        create_users = """
        INSERT INTO
          {5} (id,DataTime, Temperature1, Temperamure2, Humidity)
        VALUES
          ({0},'{1}',{2},{3},{4});
        """.format(id,DataTime, temp1, temp2, hum, data.name_db)
        self.execut_query(create_users)
        self.conn.commit()