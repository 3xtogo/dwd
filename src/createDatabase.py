import sqlite3
import json
import os


def createTables(cur):
    """
    creates default tables for database
    :param cur: cursor of sqlite3
    :return: none
    """
    cur.execute("""CREATE TABLE "Tuerschild" (
                                "Raum ID"   TEXT,
                                "jsonFormat" TEXT,                    
                                PRIMARY KEY("Raum ID")
                                )""")

    cur.execute("""CREATE TABLE "Person" (
                            "lastName"  TEXT,
                            "firstName" TEXT,
                            "picture"   BLOB,
                            "text"      TEXT,
                            PRIMARY KEY("firstName","lastName")
                            )""")

    cur.execute("""CREATE TABLE "Events" (
                            "id"	    TEXT,
                            "ics"	    BLOB,
                            PRIMARY KEY("id")
                            )""")


def dropAllTables(cur):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    print('tables:', tables)

    for table in tables:
        cur.execute("DROP TABLE {}".format(table[0]))


def createEntryFromJson(cur, myJsonFile):
    """

    :param cur: sqlite3 cursor
    :param myJsonFile: path to a json file
    :return:
    """
    # print(os.listdir())
    with open(myJsonFile) as f:
        jObj = json.load(f)
        print('jObj', jObj)


def mainCreateDatabase():
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
