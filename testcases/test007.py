from openpyxl import load_workbook
from common.test_data_handler import get_test_data_from_excel

cases = get_test_data_from_excel('../testdata/absdata.xlsx', 'Sheet1')
print(cases)