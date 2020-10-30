import xlrd

loc = ("c:\\Users\\Praveen\\Desktop\\Test_Py.xlsx")

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)
 
# For row 0 and column 0
print(sheet.cell_value(0, 0))

print(sheet.nrows)

print(sheet.ncols)

#all column names
for i in range (sheet.ncols):
    print(sheet.cell_value(0, i))

#first column
for i in range (sheet.nrows):
    print(sheet.cell_value(i,0))

#row values
for i in range (sheet.nrows):
    print(sheet.row_values(i))