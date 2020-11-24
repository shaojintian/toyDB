import pandas
import json
from constant import *
from data_structure import *


class DBEngine:
    def __init__(self):
        pass

    def readTableFromFile(self,filepath,format=DataFormat.CSV):
        if format == DataFormat.CSV:
            return csvToRowSet(filepath)
        elif format == DataFormat.JSON:
            return jsonToRowSet(filepath)
        assert False # can not reach here

    def limitOperator(self,rowSet,limitSize):
        return RowSet(rowSet.rows[:limitSize])

    def




