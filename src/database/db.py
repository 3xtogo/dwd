import psycopg2
from database.config import config
from helper.functions import timeStamp

class Db:
    def __init__(self):
        self.conn = None
        self.cur = None
        params = config()

        print(timeStamp(), 'Connected to the PostgreSQL database')
        conn = psycopg2.connect(**params)

        # create a cursor
        # cur = conn.cursor()


if __name__ == '__main__':
    db = Db()
