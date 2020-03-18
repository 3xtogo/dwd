import sqlite3
import json
import os

def createTables(cur):
    """
    creates default tables for database
    :param cur: cursor of sqlite3
    :return: none
    """
    cursor.execute("""CREATE TABLE "Tuerschild" (
                                "Raum ID"   TEXT,
                                "integer1"  INTEGER,
                                "text1"	    TEXT,
                                "blob1"	    BLOB,
                                "real1"	    REAL,
                                "numeric1"	NUMERIC,
                                PRIMARY KEY("Raum ID")
                                )""")

    cursor.execute("""CREATE TABLE "Person" (
                            "lastName"  TEXT,
                            "firstName" TEXT,
                            "picture"   BLOB,
                            "text"      TEXT,
                            PRIMARY KEY("firstName","lastName")
                            )""")

    cursor.execute("""CREATE TABLE "Events" (
                            "id"	    TEXT,
                            "ics"	    BLOB,
                            PRIMARY KEY("id")
                            )""")


def dropAllTables(cur):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print('tables:', tables)

    for table in tables:
        cursor.execute("DROP TABLE {}".format(table[0]))


def createEntryFromJson(cur, myJsonFile):
    """

    :param cur: sqlite3 cursor
    :param myJsonFile: path to a json file
    :return:
    """
    #print(os.listdir())
    with open(myJsonFile) as f:
        jObj = json.load(f)
        print('jObj', jObj)

if __name__ == '__main__':
    localDbPath = r".\database\localApplicationDatabase.db"
    connection = sqlite3.connect(localDbPath)
    print('connected to', localDbPath)

    cursor = connection.cursor()

    dropAllTables(cursor)
    connection.commit()
    createTables(cursor)

    createEntryFromJson(cursor, r"layout.json")

    connection.commit()
    cursor.close()
    connection.close()
