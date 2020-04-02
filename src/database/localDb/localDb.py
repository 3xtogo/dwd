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
    def addDozent(self, ID, Vorname, Nachname, Sprechzeiten, E_Mail, Telefonnummer, StudIP_Link, RaumNr, DisplayID):
        sql = """INSERT INTO {} 
VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {})""" \
            .format(Dozenten_Table().name,
                    ID, Vorname, Nachname, Sprechzeiten, E_Mail, Telefonnummer, StudIP_Link, RaumNr, DisplayID)
        print(sql)
        self.cursor.execute(sql)

    def addKalender(self, ID, WochentagTag, StartUhrzeit, Ereignis, RaumID):
        sql = """INSERT INTO {} 
        VALUES ()""" \
            .format(Kalender_Table().name, ID, WochentagTag, StartUhrzeit, Ereignis, RaumID)
        print(sql)
        self.cursor.execute(sql)

    def addRaum(self, ID, Bezeichnung, Typ, AnzPlaetze, Gebaeude, Fachbereich, Studienbereich):
        sql = """INSERT INTO {} 
        VALUES ()""" \
            .format(Raum_Table().name, ID, Bezeichnung, Typ, AnzPlaetze, Gebaeude, Fachbereich, Studienbereich)
        self.cursor.execute(sql)

    def addDisplay(self, ID, RaumID):
        sql = """INSERT INTO {} 
        VALUES ()""" \
            .format(Display_Table().name, ID, RaumID)
        self.cursor.execute(sql)

    def addInformationen(self, ID, InfoText, AnzeigeDauer, DozID):
        sql = """INSERT INTO {} 
        VALUES ()""" \
            .format(Informationen_Table().name, ID, InfoText, AnzeigeDauer, DozID)
        self.cursor.execute(sql)

    def addExampleData(self):
        self.addDozent(1, "'Visar'", "'Januzaj'", "'Fr-10:00-12:00'", "'visar.januzaj@hs-rm.de'", "'0160123456'",
                       "'url'", "'A123'", 1)

        pass


if __name__ == '__main__':
    ldb = LocalDb()
    ldb.dropAllTables()
    ldb.createTables()

    print('all Tables\n', ldb.getAllTablesFromDb())
    ldb.addExampleData()
    ldb.commit()
    ldb.close()
