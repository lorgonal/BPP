import csv
import json

import pandas as pd
from fastapi import FastAPI
from starlette.responses import FileResponse

import ml
from iris_model import IrisClass

app = FastAPI()
FILE_PATH = 'iris.csv'
FIELD_NAMES = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
PLOT_NAME = 'plot.png'
y_pred = None
y_test = None


# TODO
# Cambiar raiz

@app.get("/")
async def root():
    """
    Muestra una vista de prueba en /
    :return:
    """
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """
    Muestra una vista que escribe 'Hello {name} en /hello/{name}
    :param name: str
    Nombre a mostrar
    :return: str
    """
    return {"message": f"Hello {name}"}


@app.get('/iris/')
async def get_iris():
    """
    Carga el iris dataset
    :return: json
    """
    x_df = pd.read_csv(FILE_PATH)
    data = x_df.to_json(orient='index')
    data = json.loads(data)
    return data


@app.post('/iris/')
async def add_iris(iris: IrisClass):
    """
    Añade un nuevo iris al dataset
    :param iris: IrisClass
    Nuevo Iris a insertar
    :return: IrisClass
    """
    with open(FILE_PATH, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
        iris_dic = {}
        for name in FIELD_NAMES:
            iris_dic[name] = getattr(iris, name)
        writer.writerow(iris_dic)
    return iris


@app.put('/iris/')
async def update_iris(iris: IrisClass):
    """
    Actualiza el último iris en el dataset
    :param iris: IrisClass
    Datos del iris a actualizar
    :return: json
    """
    df = pd.read_csv(FILE_PATH)
    for name in FIELD_NAMES:
        df.loc[df.index[-1], name] = getattr(iris, name)
    df.to_csv(FILE_PATH, index=False)
    return df.iloc[-1].to_json(orient='index')


@app.delete('/iris/')
async def delete_iris():
    """
    Elimina el último iris del dataset
    :return: str
    """
    df = pd.read_csv(FILE_PATH)
    df.drop(df.index[-1], inplace=True)
    df.to_csv(FILE_PATH, index=False)
    return 'Deleted'


@app.get('/prediction/')
async def get_prediction():
    """
    Obtiene la predicción
    :return: str
    """
    df = ml.load_df(FILE_PATH)
    global y_pred
    global y_test
    y_pred, y_test = ml.prediction(df)
    response = ''
    for i in y_pred:
        response += f' {i}'
    return response


@app.get('/accuracy/')
async def get_accuracy():
    """
    Obtiene la precisión de la predición o error si no se ha realizado
    :return: float, str
    """
    if y_pred is not None:
        return ml.accuracy(y_test, y_pred)
    else:
        return 'First get prediction'


@app.get('/plot/', responses={
    200: {
        "content": {"image/png": {}}
    }
},
         response_class=FileResponse, )
async def get_plot():
    """
    Pinta el plot del dataset
    :return:
    """
    df = ml.load_df(FILE_PATH)
    ml.create_plot(PLOT_NAME, df)
    return FileResponse(PLOT_NAME)
