import cx_Oracle
import os
import sys
import pyodbc

# Connect as user "scott" with password "TIGER" to the "orcl" service running on this computer.
connection = cx_Oracle.connect("scott", "TIGER", "localhost/orcl")

cursor = connection.cursor()
cursor.execute("""
        SELECT empno, ename
        FROM emp
        WHERE mgr = :mg""",
        mg = 7698)
for empno, ename in cursor:
    print("Values:", empno, ename)