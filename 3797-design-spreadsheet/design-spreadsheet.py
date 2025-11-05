class Spreadsheet:

    def __init__(self, rows: int):
        # 26 (A to Z) cols and * rows
        # lets do a cols dict -> rows dict
        self.rowCount = rows
        self.cols = {} # A -> rows

        for i in range(26):
            c = chr(i + ord("A"))
            self.cols[c] = [0] * rows
        # print(self.cols)

        

    def setCell(self, cell: str, value: int) -> None:
        # given as string A10, set a value
        c = cell[0]
        row = int(cell[1:]) - 1 # row 1 is index 0
        self.cols[c][row] = value

        

    def resetCell(self, cell: str) -> None:
        # set to 0
        self.setCell(cell, 0)
    
    def getCell(self, cell):
        # print(cell)
        c = cell[0]
        row = int(cell[1:]) - 1 # row 1 is index 0
        return self.cols[c][row]

    def getValue(self, formula: str) -> int:
        # always in the form =X+Y, 
        s = formula[1:]
        arr = s.split('+')
        x, y = arr[0], arr[1]
        xVal, yVal = 0, 0

        if x.isnumeric():
            xVal = int(x)
        else:
            xVal = self.getCell(x)
        if y.isnumeric():
            yVal = int(y)
        else:
            yVal = self.getCell(y)
        
        return xVal + yVal

        
# 20:03


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)