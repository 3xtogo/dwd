import psycopg2
from database.config import config


class Db:
    def __init__(self):
        self.conn = None
        self.cur = None
        params = config()

        print('Connecting to the PostgreSQL database')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        print('Connecting to the PostgreSQL database')


if __name__ == '__main__':
    db = Db()
