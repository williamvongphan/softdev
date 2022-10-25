"""
QR Code Generators: William Vongphanith, Julia Lee, and Jeffrey Zou
"""

import sqlite3  # enable control of an sqlite database
import csv  # facilitate CSV I/O


debug = False  # set to True to print debug messages


def insert(cursor, table, columns, values):
    """
    Inserts a row into a table

    Args:
        cursor (sqlite3.Cursor): cursor to execute commands
        table (str): name of table
        columns (list): list of column names
        values (list): list of values to be inserted
    """
    # create the command
    sql_command = "INSERT INTO " + table + " (" + ", ".join(columns) + ") VALUES (" + ", ".join(
        ["?"] * len(values)) + ")"
    # execute the command
    cursor.execute(sql_command, values)
    if debug:
        print("Inserted", values, "into", table)


def get_one(cursor, table, column, value):
    """
    Gets one row from a table

    Args:
        cursor (sqlite3.Cursor): cursor to execute commands
        table (str): name of table
        column (str): name of column
        value (str): value to be searched for

    Returns:
        list: row
    """
    # create the command
    sql_command = "SELECT * FROM " + table + " WHERE " + column + " = ?"
    # execute the command
    cursor.execute(sql_command, (value,))
    # return the row
    response = cursor.fetchone()
    if debug:
        print("Got", response, "from", table)
    return response


def create_table(cursor, table, columns):
    """
    Creates a table

    Args:
        cursor (sqlite3.Cursor): cursor to execute commands
        table (str): name of table
        columns (list): list of column names
    """
    # create the command
    sql_command = "CREATE TABLE " + table + " (" + ", ".join(columns) + ")"
    # execute the command
    if debug:
        print("Created", table)
    cursor.execute(sql_command)


def clear_table(cursor, table):
    """
    Clears a table

    Args:
        cursor (sqlite3.Cursor): cursor to execute commands
        table (str): name of table
    """
    # create the command
    sql_command = "DELETE FROM " + table
    # execute the command
    if debug:
        print("Cleared", table)
    cursor.execute(sql_command)


DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
c = db.cursor()  # facilitate db ops -- you will use cursor to trigger db events

# ==========================================================

database_list = ["courses", "students"]

for database in database_list:
    # Open the csv file
    with open(database + ".csv", newline='') as csvfile:
        # read that dict
        reader = csv.DictReader(csvfile)
        # check if the table exists
        table_exists = get_one(c, "sqlite_master", "name", database)
        # if the table doesn't exist
        if not table_exists:
            # create the table
            create_table(c, database, list(reader.fieldnames))
        else:
            # clear the table
            clear_table(c, database)
        # for each row
        for row in reader:
            # insert the row
            insert(c, database, list(row.keys()), list(row.values()))

# ==========================================================

db.commit()  # save changes
db.close()  # close database
