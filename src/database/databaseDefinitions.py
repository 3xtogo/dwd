#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Autor: 3xtogo
    Status: Development
    Description: Definition for Database Charts and Objects related to tablecolums
"""

from typing import List


class Datatype:
    # CHAR = 'CHAR'
    # VARCHAR = 'VARCHAR'
    # TINYTEXT = 'TINYTEXT'
    TEXT = 'TEXT'
    BLOB = 'BLOB'
    # MEDIUMTEXT = 'MEDIUMTEXT'
    # MEDIUMBLOB = 'MEDIUMBLOB'
    # LONGTEXT = 'LONGTEXT'
    # LONGBLOB = 'LONGBLOB'
    # TINYINT = 'TINYINT'
    # SMALLINT = 'SMALLINT'
    # MEDIUMINT = 'MEDIUMINT'
    INT = 'INT'
    # BIGINT = 'BIGINT'
    FLOAT = 'FLOAT'
    # DOUBLE = 'DOUBLE'
    # DECIMAL = 'DECIMAL'
    # DATEDATETIME = 'DATEDATETIME'
    # TIMESTAMP = 'TIMESTAMP'
    TIME = 'TIME'
    # ENUM = 'ENUM'
    # SET = 'SET'
    BOOLEAN = 'BOOLEAN'


class Column:
    def __init__(self, name, dataType, isPrimaryKey=False):
        self.name = name
        self.dataType = dataType
        self.isPrimaryKey = isPrimaryKey


class Table:
    def __init__(self, name):
        self.name = name
        self.columns = []

    def defineColumn(self, column):
        self.columns.append(column)

    def primaryKey(self):
        primaryKey = []
        for col in self.columns:
            if col.isPrimaryKey:
                return col
        return None


class Dozent:
    def __init__(self, ID, Vorname, Nachname, Sprechzeiten, E_Mail, Telefonnummer, StudIP_Link, RaumNr, DisplayID):
        self.ID = ID
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Sprechzeiten = Sprechzeiten
        self.E_Mail = E_Mail
        self.Telefonnummer = Telefonnummer
        self.StudIP_Link = StudIP_Link
        self.RaumNr = RaumNr
        self.DisplayID = DisplayID

    def sqlInsert(self):
        sql = """INSERT INTO {} 
        VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {})""" \
            .format(Dozenten_Table().name,
                    self.ID,
                    self.Vorname,
                    self.Nachname,
                    self.Sprechzeiten,
                    self.E_Mail,
                    self.Telefonnummer,
                    self.StudIP_Link,
                    self.RaumNr,
                    self.DisplayID)
        return sql

    @staticmethod
    def fromQuery(query):
        ID, Vorname, Nachname, Sprechzeiten, E_Mail, Telefonnummer, StudIP_Link, RaumNr, DisplayID = query[0]
        return Dozent(ID, Vorname, Nachname, Sprechzeiten, E_Mail, Telefonnummer, StudIP_Link, RaumNr, DisplayID)


class Dozenten_Table(Table):
    def __init__(self):
        Table.__init__(self, 'Dozenten')
        self.defineColumn(Column('ID', Datatype.INT, isPrimaryKey=True))
        self.defineColumn(Column('Vorname', Datatype.TEXT))
        self.defineColumn(Column('Nachname', Datatype.TEXT))
        self.defineColumn(Column('Sprechzeiten', Datatype.BLOB))
        self.defineColumn(Column('E_Mail', Datatype.TEXT))
        self.defineColumn(Column('Telefonnummer', Datatype.TEXT))
        self.defineColumn(Column('StudIP_Link', Datatype.TEXT))
        self.defineColumn(Column('RaumNr', Datatype.TEXT))
        self.defineColumn(Column('DisplayID', Datatype.TEXT))


class Kalender:
    def __init__(self, ID, WochentagTag, StartUhrzeit, Endurzeit, Ereignis, RaumID):
        self.ID = ID
        self.WochentagTag = WochentagTag
        self.StartUhrzeit = StartUhrzeit
        self.Endurzeit = Endurzeit
        self.Ereignis = Ereignis
        self.RaumID = RaumID

    def sqlInsert(self):
        sql = """INSERT INTO {} 
        VALUES ({}, {}, {}, {}, {}, {})""" \
            .format(Kalender_Table().name,
                    self.ID,
                    self.WochentagTag,
                    self.StartUhrzeit,
                    self.Endurzeit,
                    self.Ereignis,
                    self.RaumID)
        return sql

    @staticmethod
    def fromQuery(queryResult):
        (ID, WochentagTag, StartUhrzeit, Endurzeit, Ereignis, RaumID) = queryResult[0]
        return Kalender(ID, WochentagTag, StartUhrzeit, Endurzeit, Ereignis, RaumID)


class Kalender_Table(Table):
    def __init__(self):
        Table.__init__(self, 'Kalender')
        self.defineColumn(Column('ID', Datatype.INT, isPrimaryKey=True))
        self.defineColumn(Column('WochentagTag', Datatype.TEXT))
        self.defineColumn(Column('StartUhrzeit', Datatype.TEXT))
        self.defineColumn(Column('Endurzeit', Datatype.TEXT))
        self.defineColumn(Column('Ereignis', Datatype.TEXT))
        self.defineColumn(Column('RaumID', Datatype.TEXT))


class Raum:
    def __init__(self, ID, Bezeichnung, Typ, AnzPlaetze, Gebaeude, Fachbereich, Studienbereich):
        self.ID = ID
        self.Bezeichnung = Bezeichnung
        self.Typ = Typ
        self.AnzPlaetze = AnzPlaetze
        self.Gebaeude = Gebaeude
        self.Fachbereich = Fachbereich
        self.Studienbereich = Studienbereich

    def sqlInsert(self):
        sql = """INSERT INTO {} 
        VALUES ({}, {}, {}, {}, {}, {}, {})""" \
            .format(Raum_Table().name,
                    self.ID,
                    self.Bezeichnung,
                    self.Typ,
                    self.AnzPlaetze,
                    self.Gebaeude,
                    self.Fachbereich,
                    self.Studienbereich)
        return sql

    @staticmethod
    def fromQuery(queryResult):
        ID, Bezeichnung, Typ, AnzPlaetze, Gebaeude, Fachbereich, Studienbereich = queryResult[0]
        return Raum(ID, Bezeichnung, Typ, AnzPlaetze, Gebaeude, Fachbereich, Studienbereich)


class Raum_Table(Table):
    def __init__(self):
        Table.__init__(self, 'Raum')
        self.defineColumn(Column('ID', Datatype.TEXT, isPrimaryKey=True))
        self.defineColumn(Column('Bezeichnung', Datatype.TEXT))
        self.defineColumn(Column('Typ', Datatype.TEXT))
        self.defineColumn(Column('AnzPlaetze', Datatype.TEXT))
        self.defineColumn(Column('Gebaeude', Datatype.TEXT))
        self.defineColumn(Column('Fachbereich', Datatype.TEXT))
        self.defineColumn(Column('Studienbereich', Datatype.TEXT))


class Display:
    def __init__(self, ID, RaumID, Json):
        self.ID = ID
        self.RaumID = RaumID
        self.Json = Json

    def sqlInsert(self):
        sql = """INSERT INTO {} 
        VALUES ({}, {}, {})""" \
            .format(Display_Table().name,
                    self.ID,
                    self.RaumID,
                    self.Json)
        return sql

    @staticmethod
    def fromQuery(query):
        ID, RaumID, Json = query[0]
        return Display(ID, RaumID, Json)


class Display_Table(Table):
    def __init__(self):
        Table.__init__(self, 'Display')
        self.defineColumn(Column('ID', Datatype.INT, isPrimaryKey=True))
        self.defineColumn(Column('RaumID', Datatype.INT))
        self.defineColumn(Column('Json', Datatype.BLOB))


class Information:
    def __init__(self, ID, InfoText, AnzeigeDauer, DozID):
        self.ID = ID
        self.InfoText = InfoText
        self.AnzeigeDauer = AnzeigeDauer
        self.DozID = DozID

    def sqlInsert(self):
        sql = """INSERT INTO {} 
        VALUES ({}, {}, {}, {})""" \
            .format(Informationen_Table().name,
                    self.ID,
                    self.InfoText,
                    self.AnzeigeDauer,
                    self.DozID)
        return sql

    @staticmethod
    def fromQuery(sqlQuery):
        (ID, InfoText, AnzeigeDauer, DozID) = sqlQuery[0]
        return Information(ID, InfoText, AnzeigeDauer, DozID)


class Informationen_Table(Table):
    def __init__(self):
        Table.__init__(self, 'Informationen')
        self.defineColumn(Column('ID', Datatype.INT, isPrimaryKey=True))
        self.defineColumn(Column('InfoText', Datatype.TEXT))
        self.defineColumn(Column('AnzeigeDauer', Datatype.TEXT))
        self.defineColumn(Column('DozID', Datatype.TEXT))


class Media:
    def __init__(self, ID, MediaDump, MediaType):
        self.ID = ID
        self.MediaDump = MediaDump
        self.MediaType = MediaType

    def sqlInsert(self):
        sql = """INSERT INTO {} 
        VALUES ({}, {}, {})""" \
            .format(Media_Table().name,
                    self.ID,
                    self.MediaDump,
                    self.MediaType)
        return sql


class Media_Table(Table):
    def __init__(self):
        Table.__init__(self, 'Media')
        self.defineColumn(Column('ID', Datatype.INT, isPrimaryKey=True))
        self.defineColumn(Column('MediaDump', Datatype.BLOB))
        self.defineColumn(Column('MediaType', Datatype.TEXT))


if __name__ == '__main__':
    tables = [Dozenten_Table(),
              Kalender_Table(),
              Raum_Table(),
              Display_Table(),
              Informationen_Table()]

    tab: Table
    for tab in tables:
        print([column.name for column in tab.columns])
