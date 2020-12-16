import sys
import sqlite3
from sqlite3 import Error
from PyQt5 import QtWidgets
from GUI.login_screen import LoginScreenGUI
from Database.database_create import create_default_tables
from Database.database_queries import get_all_address


def create_connection(db_file):
    """
    create a database connection to the SQLite database specified by db_file
    Parameters:
        db_file: database file
    Returns:
        conn: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        create_default_tables(conn)
        return conn
    except Error as e:
        print(e)
        return None


'''
def showLogin():
    win = uic.loadUi("GUI/login_screen.ui")
    win.show()
    return win
'''

if __name__ == "__main__":
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()

    mainform = QtWidgets.QMainWindow()
    db_conn = create_connection('ecomm.sql')
    ui = LoginScreenGUI(db_conn, mainform)
    mainform.show()
    sys.exit(app.exec())
