"""
DATABASE_MANAGER.PY
"""

import sqlite3

class DatabaseManager:
    def __init__(self):
        self.con = sqlite3.connect("company.db")
        self.cur = self.con.cursor()
        

    def execute_query(self, query):
        exec_query = self.cur.execute(query)
        res = exec_query.fetchall()
        return res
