import pandas as pd
import Exceptions as ex

FILE_NAME = 'finanzas2020.csv'


def calc_exp(df):
    df2 = pd.DataFrame(columns=df.columns)
    # row 0 for negative sum
    # row 1 for positive sum
    # row 2 for negative + positive
    for col in df:
        groupRes = df.groupby(df[col])

        # lambda function
        def plus(val): return val[val > 0].sum()

        def minus(val): return val[val < 0].sum()

        exp = groupRes[col].agg([('neg', minus), ('pos', plus)])

        df2[col] = [exp['neg'].sum(), exp['pos'].sum(), exp['neg'].sum() + exp['pos'].sum()]

    return df2


def print_exp(df):
    max_val_index = df.idxmax(axis=1)
    min_val_index = df.idxmin(axis=1)
    tot_exp=df.sum(axis=1)
    avg_val=df.mean(axis=1)
    print(f'El mes con más gastos es: {min_val_index[0]}')
    print(f'El mes con más ingresos es: {max_val_index[1]}')
    print(f'El mes con más ahorro es: {max_val_index[2]}')
    print(f'El gasto medio es:{ avg_val[0]}')
    print(f'El gasto total ha sido {tot_exp[0]}')
    print(f'Los ingresos totales han sido {tot_exp[1]}')


def parse_file():
    try:
        df = pd.read_csv(FILE_NAME, delimiter='\t')
        #df = pd.read_csv(FILE_NAME)
        print(df.head())
        ex.validate_head_num(df)
        df = ex.validate_content(df)
        #df.to_csv('text.csv')
        print_exp(calc_exp(df))

    except IOError as e:
        print('Fichero no encontrado. ', e)


if __name__ == '__main__':
    parse_file()
