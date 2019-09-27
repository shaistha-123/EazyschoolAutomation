import xlrd, unittest
from ddt import ddt, data, unpack
from selenium import webdriver
def get_data(file_name):
       # create an empty list to store rows
       rows = []
       # open the specified Excel spreadsheet as workbook
       book = xlrd.open_workbook(file_name)
       # get the first sheet
       sheet = book.sheet_by_index(0)
       # iterate through the sheet and get data from rows in list
       for row_idx in range(1, sheet.nrows):
           rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
       return rows
@ddt
class checkddt (unittest.TestCase):
        def setUp(self):
        [Insert your setUp code here]


    # get the data from specified Excel spreadsheet
    # by calling the get_data function
    @data(*get_data("TestData.xlsx"))
    @unpack
    def test_[your_test_name](self, [your_argument_1], [your_argument_2]):
           [your test method]


    def tearDown(self):
        # close the browser window
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()