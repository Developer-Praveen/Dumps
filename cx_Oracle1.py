import cx_Oracle
import os
import sys
import pyodbc

cx_Oracle.init_oracle_client(lib_dir=r"E:\\app\\Praveen\\product\\11.2.0\\dbhome_1\\BIN")

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