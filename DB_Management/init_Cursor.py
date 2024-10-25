import pyodbc

class init_Cursor:
    def __init__(self):
        self.server = 'localhost'
        self.database = 'db'
        self.username = 'username'
        self.password = 'password'
        self.connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';Trusted_Connection=yes;'
        self.connection = pyodbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()

    def get_cursor(self):
        return self.cursor