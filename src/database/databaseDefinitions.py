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


class Dozenten_Table(Table):
    def __init__(self):
        Table.__init__(self, 'Dozenten')
        self.defineColumn(Column('ID', Datatype.INT, isPrimaryKey=True))
        self.defineColumn(Column('Vorname', Datatype.TEXT))
        self.defineColumn(Column('Nachname', Datatype.TEXT))
        self.defineColumn(Column('Sprechzeiten', Datatype.TEXT))
        self.defineColumn(Column('E_Mail', Datatype.TEXT))
        self.defineColumn(Column('Telefonnummer', Datatype.TEXT))
        self.defineColumn(Column('StudIP_Link', Datatype.TEXT))
        self.defineColumn(Column('RaumNr', Datatype.TEXT))
        self.defineColumn(Column('DisplayID', Datatype.TEXT))


class Kalender_Table(Table):
    def __init__(self):
        Table.__init__(self, 'Kalender')
        self.defineColumn(Column('ID', Datatype.INT, isPrimaryKey=True))
        self.defineColumn(Column('WochentagTag', Datatype.TEXT))
        self.defineColumn(Column('StartUhrzeit', Datatype.TEXT))
        self.defineColumn(Column('Endurzeit', Datatype.TEXT))
        self.defineColumn(Column('Ereignis', Datatype.TEXT))
        self.defineColumn(Column('RaumID', Datatype.TEXT))


class Raum_Table(Table):
    def __init__(self):
        Table.__init__(self, 'Raum')
        self.defineColumn(Column('ID', Datatype.INT, isPrimaryKey=True))
        self.defineColumn(Column('Bezeichnung', Datatype.TEXT))
        self.defineColumn(Column('Typ', Datatype.TEXT))
        self.defineColumn(Column('AnzPlätze', Datatype.TEXT))
        self.defineColumn(Column('Gebäude', Datatype.TEXT))
        self.defineColumn(Column('Fachbereich', Datatype.TEXT))
        self.defineColumn(Column('Studienbereich', Datatype.TEXT))


class Display_Table(Table):
    def __init__(self):
        Table.__init__(self, 'Display')
        self.defineColumn(Column('ID', Datatype.INT, isPrimaryKey=True))
        self.defineColumn(Column('RaumID', Datatype.TEXT))


class Informationen_Table(Table):
    def __init__(self):
        Table.__init__(self, 'Informationen')
        self.defineColumn(Column('ID', Datatype.INT, isPrimaryKey=True))
        self.defineColumn(Column('InfoText', Datatype.TEXT))
        self.defineColumn(Column('AnzeigeDauer', Datatype.TEXT))
        self.defineColumn(Column('DozID', Datatype.TEXT))

class Media_Table(Table):
    def __init__(self):
        Table.__init__(self, 'Media')
        self.defineColumn(Column('ID', Datatype.INT, isPrimaryKey=True))
        self.defineColumn(Column('Media', Datatype.BLOB))



if __name__ == '__main__':
    tables = [Dozenten_Table(),
              Kalender_Table(),
              Raum_Table(),
              Display_Table(),
              Informationen_Table()]

    for tab in tables:
        print(tab.name, tab.columnOptions())
