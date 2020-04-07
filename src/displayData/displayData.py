from database.localDb.localDb import LocalDb


class DisplayData:
    def __init__(self, displayId):
        self.displayId = displayId

        self.localDb = LocalDb()

        self.testFuncDb()

    def testFuncDb(self):
        print(self.localDb.listTables())
        sql = """SELECT * FROM Display WHERE Display.ID={}""".format(self.displayId)
        self.localDb.cursor.execute(sql)
        print(self.localDb.cursor.fetchall())
