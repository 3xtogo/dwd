import sqlite3
import json
from helper.functions import timeStamp


class DbReader:
    def __init__(self, pathToLocalDb):
        self.connection = sqlite3.connect(pathToLocalDb)
        self.cursor = self.connection.cursor()

    def listTables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        return tables

    def deleteAllTables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        print('tables:', tables)

        for table in tables:
            self.cursor.execute("DROP TABLE {}".format(table[0]))

    def createDefaultDatabaseLocal(self):
        self.deleteAllTables()

        tableName = "Tuerschild"
        primaryKey = "RaumID"
        jsonName = "jsonFormat"
        jsonStr = None
        self.cursor.execute("""CREATE TABLE "{}" (
                                        "{}"   TEXT,
                                        "jsonFormat" TEXT,                    
                                        PRIMARY KEY("Raum ID")
                                        )""".format(tableName, primaryKey, jsonName))

        with open('layout.json', 'r') as f:
            jsonStr = f.read()

        self.cursor.execute("""INSERT INTO "{}"
        """.format(tableName,))
        print(jsonStr)

        # self.cursor.execute("""CREATE TABLE "Person" (
        #                             "lastName"  TEXT,
        #                             "firstName" TEXT,
        #                             "picture"   BLOB,
        #                             "text"      TEXT,
        #                             PRIMARY KEY("firstName","lastName")
        #                             )""")
        #
        # self.cursor.execute("""CREATE TABLE "Events" (
        #                             "id"	    TEXT,
        #                             "ics"	    BLOB,
        #                             PRIMARY KEY("id")
        #                             )""")

    def commitAndClose(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


if __name__ == '__main__':
    myPath = r"localApplicationDatabase.db"
    myDb = DbReader(myPath)
    myDb.createDefaultDatabaseLocal()
    myDb.listTables()
    print(myDb.listTables())
