#@PydevCodeAnalysisIgnore
import sqlite3

from common.Constants import Constants
#from db.SeriousGames import SeriousGames

class DatabaseHelper:

#    db = SeriousGames()

    @staticmethod
    def dbSelectRowByID(table, attribute, value):
        """Generic method to fetch contents from the local database."""
        connection = sqlite3.connect(Constants.DATABASE)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        query = 'SELECT * FROM ' + table + ' WHERE ' + attribute + ' = ' + str(value)
        cursor.execute(query)

        return cursor.fetchone()

#        tableList = {}
#
#        table = DatabaseHelper.db.getTable(table)
#
#        if table != None:
#            if value in table[1]:
#                tableList[table[0][0]] = value
#
#                record = table[1][value]
#
#                for i in range(1, len(table[0])):
#                    tableList[table[0][i]] = record[i - 1]
#
#        return tableList

    @staticmethod
    def dbUpdate(table, key_name, key_id, attribute, value):
        """ Generic mathod to update data in table with the key_name matches key_id """
        connection = sqlite3.connect(Constants.DATABASE)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        query = 'UPDATE ' + table + ' SET ' + attribute + ' = ' + str(value) + ' WHERE ' + key_name + ' = ' + str(key_id)
        cursor.execute(query)

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def dbInsert(table, *args):
        """ Generic method to insert an array of args to database table """
        connection = sqlite3.connect(Constants.DATABASE)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        query = 'INSERT INTO ' + table + ' VALUES (\'' + str(args[0]) + '\''

        for i in range(1, len(args)):
            query += ', \'' + str(args[i]) + '\''

        query += ')'

        cursor.execute(query)

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def dbGetRowCount(table):
        """Generic method to return the number of items from the local database."""
        connection = sqlite3.connect(Constants.DATABASE)
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        query = 'SELECT * FROM ' + table
        cursor.execute(query)

        return len(cursor.fetchall())

#        table = DatabaseHelper.db.getTable(table)
#
#        if table != None:
#            return len(table[1])
#
#        return 0
