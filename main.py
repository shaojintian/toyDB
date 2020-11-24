from engine import  DBEngine
from constant import DataFormat
if __name__ == '__main__':
    engine = DBEngine()
    engine.readTableFromFile(filepath='./metaDataJSON.txt',format=DataFormat.JSON)
