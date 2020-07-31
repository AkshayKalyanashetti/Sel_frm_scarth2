import xlrd
def get_val(sheet_name, input_val):
    wb = xlrd.open_workbook("C:\\Users\\Akshay\\Downloads\\Book.xlsx")
    ws = wb.sheet_by_name(sheet_name)
    row_count = ws.nrows
    col_count = ws.ncols
    for i in range(row_count):
        for j in range(col_count):
            if ws.cell_value(i, j) == input_val:
                print(ws.cell_value(i + 1, j))

get_val("Sheet1", "Name")
