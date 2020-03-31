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

    ### ADD Data

    def addDozent(self, ID, Vorname, Nachname, Sprechzeiten, E_Mail, Telefonnummer, StudIP_Link, RaumNr, DisplayID):
        pass

    def addKalender(self, ID, WochentagTag, StartUhrzeit, Endurzeit, Ereignis, RaumID):
        pass

    def addRaum(self, ID, Bezeichnung, Typ, AnzPlaetze, Gebaeude, Fachbereich, Studienbereich):
        pass

    def addDisplay(self, ID, RaumID):
        pass

    def addInformationen(self, ID, InfoText, AnzeigeDauer, DozID):
        pass


if __name__ == '__main__':
    ldb = LocalDb()
    ldb.dropAllTables()
    ldb.createTables()
    ldb.commit()
    print('all Tables\n', ldb.getAllTablesFromDb())
    ldb.close()
