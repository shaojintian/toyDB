import pandas
import json
from constant import *
class DBEngine:
    def __init__(self):
        pass

    def readTableFromFile(self,filepath,format=DataFormat.CSV):
        if format == DataFormat.CSV:
            return csvToRowSet(filepath)
        elif format == DataFormat.JSON:
            return jsonToRowSet(filepath)
        assert False # can not reach here


def csvToRowSet(filepath):



def jsonToRowSet(filepath):
    with open(filepath) as json_file:
        data = json.load(json_file)

