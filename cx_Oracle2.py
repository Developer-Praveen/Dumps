import cx_Oracle
import os
import sys
import pyodbc

cx_Oracle.init_oracle_client(lib_dir=r"E:\\app\\Praveen\\product\\11.2.0\\dbhome_1\\BIN")

print(sys.version)
#print(os.environ['ORACLE_HOME'])
print(os.environ['path'])

con = cx_Oracle.connect("scott", "TIGER", "localhost/orcl")
print (con.version)
print ("DONE")

con.close()