import pandas as pd


class ColNumberError(Exception):
    """Exception raised for errors in the number of columns.

    Attributes:
        col_num -- head count that caused the error
    """

    def __init__(self, col_num):
        super().__init__(f'Columnas definidas: {col_num}. El número esperado es 12')


class NoData(Exception):
    """Exception raised when column has no data

    Attributes:
        column -- name of the column with no data
    """

    def __init__(self, column):
        super().__init__(f'La columna {column} no tiene datos')
