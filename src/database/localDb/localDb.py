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

    def listTables(self):
        sql = """SELECT name FROM sqlite_master WHERE type='table'"""
        self.cursor.execute(sql)
        return [result[0] for result in self.cursor.fetchall()]

    def dropAllTables(self):
        for table in self.listTables():
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

    def joinTables(self):
        sql = """JOIN SOMETHING"""
        self.cursor.execute(sql)

    def exampleData(self):
        self.addDozent(Dozent(ID=1,
                              Vorname="'Visar'",
                              Nachname="'Januzaj'",
                              Sprechzeiten="'Fr_10_00_12_00'",
                              E_Mail="'visar.januzaj@hs-rm.de'",
                              Telefonnummer="'0160123456'",
                              StudIP_Link="'url'",
                              RaumNr="'A123'",
                              DisplayID=1))

        self.addDozent(Dozent(ID=2,
                              Vorname="'Andreas'",
                              Nachname="'Zinnen'",
                              Sprechzeiten="'Di_10_00_12_00'",
                              E_Mail="'andreas.zinnen@hs-rm.de'",
                              Telefonnummer="'0160123465'",
                              StudIP_Link="'url2'",
                              RaumNr="'A123'",
                              DisplayID=1))

        self.addDozent(Dozent(ID=3,
                              Vorname="'Some'",
                              Nachname="'OtherDozent'",
                              Sprechzeiten="'Mo_08_15_12_00'",
                              E_Mail="'ha_myNameis@hs-rm.de'",
                              Telefonnummer="'0160121465'",
                              StudIP_Link="'url3'",
                              RaumNr="'A123'",
                              DisplayID=1))

        self.addKalender(Kalender(ID=1,
                                  WochentagTag="'MO'",
                                  StartUhrzeit="'10:00'",
                                  Endurzeit="'11:30'",
                                  Ereignis="'iOOP'",
                                  RaumID=1))

        self.addKalender(Kalender(ID=2,
                                  WochentagTag="'MO'",
                                  StartUhrzeit="'10:00'",
                                  Endurzeit="'11:30'",
                                  Ereignis="'iOOP'",
                                  RaumID=1))

        self.addKalender(Kalender(ID=3,
                                  WochentagTag="'Do'",
                                  StartUhrzeit="'11:00'",
                                  Endurzeit="'11:31'",
                                  Ereignis="'paralellOOP'",
                                  RaumID=2))

        self.addRaum(Raum(1, "'A127'", "'Büro'", 3, "'A1'", "'ING'", "'U&D'"))
        self.addRaum(Raum(2, "'A123'", "'Seminar'", 3, "'A1'", "'ING'", "'U&D'"))

        self.addDisplay(Display(1, 1, """'{"bar":1}'"""))  # display 1 points to room 1
        self.addDisplay(Display(2, 2, """'{"foo":2}'"""))  # display 2 points to room 2

        self.addInformationen(Information(1, "'Das ist die erste Nachricht'", "'1h'", 1))  # last param is dozID
        self.addInformationen(Information(2, "'Das ist die zweite Nachricht'", "'3.5h'", 1))  # last param is dozID
        self.addInformationen(Information(3, "'Das ist die zweite Nachricht'", "'3.3h'", 2))
        self.addInformationen(Information(4, "'Das ist die zweite Nachricht'", "'3.1h'", 2))
        pass


if __name__ == '__main__':
    ldb = LocalDb()
    ldb.dropAllTables()
    ldb.createTables()

    print('all Tables:', ldb.listTables())
    ldb.exampleData()
    ldb.commit()
    ldb.close()
