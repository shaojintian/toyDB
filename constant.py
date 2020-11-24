import enum


@enum.unique
class DataFormat(enum.Enum):
    CSV = 0
    JSON = 1
