from openpyxl import Workbook

wp = Workbook()
ws = wp.active

ws1= wp.create_sheet("Sheet1")
ws.title = "demo calass"
wp.save(filename="first_test.xlsx")
wp.close()