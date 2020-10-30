import cx_Oracle
import os
import sys
import pyodbc

print(sys.version)
#print(os.environ['ORACLE_HOME'])
print(os.environ['path'])

con = cx_Oracle.connect("scott", "TIGER", "localhost/orcl")
print (con.version)
print ("DONE")

con.close()