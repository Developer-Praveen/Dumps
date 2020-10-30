import cx_Oracle
import sys

try:
    cx_Oracle.init_oracle_client(lib_dir=r"E:\\app\\Praveen\\product\\11.2.0\\dbhome_1\\BIN")
except Exception as err:
    print("Whoops!")
    print(err)
    sys.exit(1)

print("DONE")

print(sys.version)

con = cx_Oracle.connect("scott", "TIGER", "localhost/orcl")
print (con.version)

cursor = con.cursor()

cursor.execute("""
        SELECT empno, ename, mgr
        FROM emp
        WHERE mgr = :mg""",
        mg = 7698)
for empno, ename, mgr in cursor:
    print("Values:", empno, ename, mgr)