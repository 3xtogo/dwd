import datetime


def printSQL(query, result):
    print('===========')
    print('Query:', query, '\nResult:', result)
    print('===========')


def timeStamp():
    return '[{}]'.format(datetime.datetime.now())
