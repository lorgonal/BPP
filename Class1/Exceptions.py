import pandas as pd
import re


class ColNumberError(Exception):
    """Exception raised for errors in the number of columns.

    Attributes:
        col_num -- head count that caused the error
    """

    def __init__(self, col_num):
        super().__init__(f'Columnas definidas: {col_num}. El número esperado es 12')


def validate_head_num(df):
    if len(df.columns) != 12:
        raise ColNumberError(col_num=df.columns)


class NoData(Exception):
    """Exceltion raised when column has no data

    Attributes:
        column -- name of the column with no data
    """

    def __init__(self, column):
        super().__init__(f'La columna {column} no tiene datos')


def validate_content(df):
    for col in df.columns:
        if len(df.index) == df[col].isna().sum():
            raise NoData(column=col)
        ex = True
        while (ex):
            try:
                df[col] = pd.to_numeric(df[col], errors='raise')
                ex = False
            except ValueError as e:
                regex = r"^.*string (.*) at position (\d+)"
                m = re.search(regex, str(e))
                val = m.group(1)
                pos = int(m.group(2))
                val = val.strip('"').strip("'")
                try:
                    val = int(val)
                except:
                    val = 0
                print(f'Datos inválidos en columna {col}. Se transformarán a {val}. Error: {e}')
                df._set_value(pos, col, val)

    return df
