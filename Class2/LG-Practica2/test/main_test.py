import pytest
import main
import os
import pandas as pd

from Exceptions import ColNumberError, NoData

def test_validate_content():
    df = pd.read_csv('ERROR_COL_DATA.csv', delimiter='\t')
    with pytest.raises(NoData):
        main.validate_content(df)
    df = pd.read_csv('finanzas2020.csv', delimiter='\t')
    df2 = main.validate_content(df)
    assert df2['Julio'][59]==-602
    assert df2['Octubre'][50] == 0


def test_validate_head_num():
    df = pd.read_csv('ERROR_COL_NUM.csv', delimiter='\t')
    with pytest.raises(ColNumberError):
        main.validate_head_num(df)


def test_parse_file(capsys):
    os.rename('finanzas2020.csv', 'TEST.csv')
    main.parse_file()
    captured = capsys.readouterr()
    os.rename('TEST.csv', 'finanzas2020.csv')
    assert captured.out.startswith('Fichero no encontrado. ')
    os.rename('finanzas2020.csv', 'BACK.csv')
    os.rename('ERROR_COL_NUM.csv', 'finanzas2020.csv')
    with pytest.raises(ColNumberError):
        main.parse_file()
    os.rename('finanzas2020.csv', 'ERROR_COL_NUM.csv')
    os.rename('BACK.csv', 'finanzas2020.csv')
    os.rename('finanzas2020.csv', 'BACK.csv')
    os.rename('ERROR_COL_DATA.csv', 'finanzas2020.csv')
    with pytest.raises(NoData):
        main.parse_file()
    os.rename('finanzas2020.csv', 'ERROR_COL_DATA.csv')
    os.rename('BACK.csv', 'finanzas2020.csv')
    main.parse_file()
    cap = capsys.readouterr()
    assert 'El mes con más gastos es: Abril' in cap.out
    assert 'El mes con más ingresos es: Enero' in cap.out
    assert 'El mes con más ahorro es: Enero' in cap.out
    assert 'El gasto medio es:-24827.833333333332' in cap.out
    assert 'El gasto total ha sido -297934' in cap.out
    assert 'Los ingresos totales han sido 280961' in cap.out

