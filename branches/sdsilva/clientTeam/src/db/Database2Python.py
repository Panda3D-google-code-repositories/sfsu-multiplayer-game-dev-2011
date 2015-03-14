import sqlite3

tableList = {}

connection = sqlite3.connect('SeriousGames.db')
connection.row_factory = sqlite3.Row

cursor = connection.cursor()
query = "SELECT * FROM sqlite_master WHERE type = 'table'"
cursor.execute(query)

for table in cursor.fetchall():
    query = 'PRAGMA table_info(' + table['name'] + ')'
    cursor.execute(query)

    rowList = {}
    columnList = []
    typeList = []

    for column in cursor.fetchall():
        columnList.append(str(column['name']))
        typeList.append(str(column['type']))

    query = 'SELECT * FROM ' + table['name']
    cursor.execute(query)

    for record in cursor.fetchall():
        recordList = []

        id_value = record[columnList[0]]

        for i in range(1, len(columnList)):
            value = record[columnList[i]]

            if typeList[i] == 'NUMERIC':
                if int(value) <= float(value):
                    recordList.append(int(value))
                else:
                    recordList.append(float(value))
            elif typeList[i] == 'INTEGER':
                recordList.append(int(value))
            else:
                recordList.append(str(value))

        rowList[id_value] = recordList

    tableList[str(table['name'])] = [columnList, rowList]

file = open('SeriousGames.py', 'w')
file.write('class SeriousGames:' + '\n\n')
file.write('    ' + 'def __init__(self):' + '\n\n')
file.write('        ' + 'self.tableList = {}' + '\n')

for table in tableList:
    file.write('\n' + '        ' + 'rowList = {}' + '\n')

    for id_value in tableList[table][1]:
        file.write('        ' + 'rowList[' + str(id_value) + '] = ' + str(tableList[table][1][id_value]) + '\n')

    file.write('        ' + 'self.tableList[\'' + table + '\'] = [' + str(tableList[table][0]) + ', rowList]' + '\n')

file.write('\n')
file.write('    ' + 'def getTable(self, name):' + '\n')
file.write('        ' + 'if name in self.tableList:' + '\n')
file.write('            ' + 'return self.tableList[name]' + '\n')

file.close()

print 'Conversion Complete!'
