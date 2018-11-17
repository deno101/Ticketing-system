#!/usr/bin/env python3

import MySQLdb as mysql
import subprocess
import platform
import sys


# TODO end program if mysql.service does not exist
class DBops:

    # create database ticketing in mysql.db
    def createdatabase(self, conn):
        print("Creating database......")
        query = 'CREATE DATABASE IF NOT EXISTS ticketing'
        cursor = conn.cursor()
        cursor.execute(query)
        new_conn = mysql.connect('localhost', 'root', '', 'ticketing')
        print("Database created successfully....\n")
        return new_conn

    # function to run migrations to the database
    def runmigrations(self):
        print("Running migrations....")
        subprocess.call(['python', 'manage.py', 'migrate'])
        print("Migrations complete...\n")

    # Check and start mysql.service in linux based operating sys
    def startmysqlservicedeb(self):
        print("Starting mysql.service in linux......")
        output = subprocess.getoutput('service mysql start')
        if output == "" or len(output) == 0:
            print("Mysql service started correctly....\n")
        else:
            print(output)
            sys.exit(0)

    # Check if exists and start mysql.service in windows
    def startmysqlservicewin(self):
        pass

    # Format the excp
    def formatexception(self, e):
        # init a variable type(list)
        if e == '':
            pass
        w = []
        w.append(e)
        fin = str(w[0])
        # split the result array into individual chars
        ls = list(fin)
        # init a control variable for the loop
        bl = False
        finalstr = '('
        for x in ls:
            if x == ',':
                bl = True
                continue
            if bl:
                finalstr += x

        return finalstr


class App(DBops):

    def __init__(self):

        # Handling sql.service does not exist
        try:
            mysql.connect('localhost', 'root', '')

        except mysql.Error as e:
            print('An Error occured .....', end = '')
            print(DBops().formatexception(e), '\n')
            if platform.system() == 'Linux':
                DBops().startmysqlservicedeb()

            elif platform.system() == 'Windows':
                DBops().startmysqlservicewin()

        # Handling database ticketing does not exist
        try:
            self.conn = mysql.connect('localhost', 'root', '', 'ticketing')

        except mysql.Error as e:
            print('An Error occured  .....', end = '')
            print(DBops().formatexception(e), '\n')
            self.conn = mysql.connect('localhost', 'root', '')
            DBops().createdatabase(self.conn)

            # run migration after creating the database
            DBops().runmigrations()
