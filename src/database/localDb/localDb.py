import sqlite3
import os
from database.databaseDefinitions import *

tables = [Dozenten_Table(),
          Kalender_Table(),
          Raum_Table(),
          Display_Table(),
          Informationen_Table()]


class LocalDb:

    def __init__(self):
        self.path, _ = os.path.split(__file__)
        self.dbName = 'localDatabase.db'
        self.dbFullPath = os.path.join(self.path, self.dbName)
        self.connection = sqlite3.connect(self.dbFullPath)
        self.cursor = self.connection.cursor()

    # noinspection PyStringFormat

    def createTables(self):
        sqls = []

        sql = ''
        for table in tables:
            sql = """CREATE TABLE {} (\n\t{} {} PRIMARY KEY""".format(
                table.name, table.primaryKey().name, table.primaryKey().dataType)

            cols = [col for col in table.columns if not col.isPrimaryKey]
            for col in cols:
                sql += ',\n\t' + col.name + ' ' + col.dataType
            sql += ')'

            self.cursor.execute(sql)

    def getAllTablesFromDb(self):
        sql = """SELECT name FROM sqlite_master WHERE type='table'"""
        self.cursor.execute(sql)
        return [result[0] for result in self.cursor.fetchall()]

    def dropAllTables(self):
        for table in self.getAllTablesFromDb():
            sql = """DROP TABLE {}""".format(table)
            self.connection.execute(sql)

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

    # ADD Data
    ##########
    def addDozent(self, dozent: Dozent):
        self.cursor.execute(dozent.sqlInsert())

    def addKalender(self, kalender: Kalender):
        self.cursor.execute(kalender.sqlInsert())

    def addRaum(self, raum: Raum):
        self.cursor.execute(raum.sqlInsert())

    def addDisplay(self, display: Display):
        self.cursor.execute(display.sqlInsert())

    def addInformationen(self, information: Information):
        self.cursor.execute(information.sqlInsert())

    def addMedia(self, media: Media):
        self.cursor.execute(media.sqlInsert())

    def exampleData(self):
        self.addDozent(Dozent(ID=1,
                              Vorname="'Visar'",
                              Nachname="'Jauzaj'",
                              Sprechzeiten="'Fr_10_00_12_00'",
                              E_Mail="'visar.januzaj@hs-rm.de'",
                              Telefonnummer="'0160123456'",
                              StudIP_Link="'url'",
                              RaumNr="'A123'",
                              DisplayID=1))
        
        self.addKalender(Kalender(ID=1,
                                  WochentagTag="'MO'",
                                  StartUhrzeit="'10:00'",
                                  Endurzeit="'11:30'",
                                  Ereignis="'iOOP'",
                                  RaumID="'A127'"))
        self.addRaum()
        self.addDisplay()
        self.addInformationen()

        pass


if __name__ == '__main__':
    ldb = LocalDb()
    ldb.dropAllTables()
    ldb.createTables()

    print('all Tables\n', ldb.getAllTablesFromDb())
    ldb.exampleData()
    ldb.commit()
    ldb.close()
