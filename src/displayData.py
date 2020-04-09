from database.localDb.localDb import LocalDb
from helperFunctions import printSQL
from database.databaseDefinitions import *


class DisplayData:
    def __init__(self, displayId):
        self.localDb = LocalDb()

        self.display = None
        self.room = None
        self.dozenten = []

        self.fetchFromLocalDb(displayId)

    def fetchFromLocalDb(self, displayId):
        print('All tables:', self.localDb.listTables())

        # display
        sqlQuery = """SELECT * FROM Display WHERE Display.ID={}""".format(displayId)
        self.localDb.cursor.execute(sqlQuery)
        queryResult = self.localDb.cursor.fetchall()
        # printSQL(sql, queryResult)
        self.display = Display.fromQuery(queryResult)

        # raum
        sqlQuery = """SELECT * FROM Raum WHERE Raum.ID={}""".format(self.display.RaumID)
        self.localDb.cursor.execute(sqlQuery)
        queryResult = self.localDb.cursor.fetchall()
        # printSQL(sqlQuery, queryResult)
        self.room = Raum.fromQuery(queryResult)
        print(self.room.__dict__)

        # dozenten
        sqlQuery = """SELECT * FROM Dozenten WHERE Dozenten.DisplayID={}""".format(displayId)