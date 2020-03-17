import sqlite3

if __name__ == '__main__':

    localDbPath = r".\database\localApplicationDatabase.db"
    connection = sqlite3.connect(localDbPath)
    print('connected to', localDbPath)

    cursor = connection.cursor()

    # delete all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print('tables:', tables)

    for table in tables:
        cursor.execute("DROP TABLE {}".format(table[0]))


    # create default table
    cursor.execute("""CREATE TABLE "tuerschild" (
                        "Raum ID"	TEXT,
                        "integer1"	INTEGER,
                        "text1"	TEXT,
                        "blob1"	BLOB,
                        "real1"	REAL,
                        "numeric1"	NUMERIC,
                        PRIMARY KEY("Raum ID")
                        )""")

    cursor.execute()


    connection.commit()
    cursor.close()
    connection.close()
