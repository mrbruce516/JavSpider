import pymysql
from pymysql import cursors


class DBConnection:
    def __init__(self, host='db', port=3306, database='scrapy', user='root', password='scrapy', charset='utf8mb4'):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.charset = charset
        self.connection  = None

    def connect(self):
        if self.connection is None:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
                charset=self.charset,
                cursorclass=cursors.DictCursor
            )
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def execute(self, sql, values=None):
        conn = self.connect()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, values)
                result = cursor.fetchall()
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            print(f"意料之外的sql执行: {e}")
            return None
