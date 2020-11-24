import json

class Cell:
    def __init__(self,type,size,val):
        self.type = type
        self.size = size
        self.val = val


class Row:
    def __init__(self,cells):
        self.cells = cells


class RowSet:
    def __init__(self,rows):
        self.rows = rows



def csvToRowSet(filepath):
    pass



def jsonToRowSet(filepath):
    rows = []
    rowSet = RowSet(rows)
    with open(filepath) as json_file:
        data = json.load(json_file)
        for metaRow in data['RowSet']:
            cells = []
            for metaCell in metaRow:
                cell = Cell(metaCell['colType'],metaCell['colSize'],metaCell['colVal'])
                cells.append(cell)
            row = Row(cells)
            rows.append(row)
        rowSet.rows = rows

    return rowSet







