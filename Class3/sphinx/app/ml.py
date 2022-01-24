import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def load_df(location):
    """
    Carga el dataset a partir de un fichero y mapea las especies a valores numéricos

    setosa: 0
    versicolor: 1
    virginica: 2

    :param location: str
    Ubicación del fichero
    :return: df DataFrame creado a partir del fichero
    """
    df = pd.read_csv(location)
    # df.drop("Id", axis=1)
    df.species = df.species.map({"setosa": 0,
                                 "versicolor": 1,
                                 "virginica": 2})
    return df


def create_plot(name, df):
    """
    Crea el plot a partir del dataframe
    :param name: str -Nombre con el que se guardará la imagen

    :param df: DataFrame - Dataframe a partir del que se genera la imagen
    :return:
    """
    sns.FacetGrid(df, hue="species", height=5.2) \
        .map(plt.scatter, "petal_length", "petal_width") \
        .add_legend()
    plt.title("Species en función del Pétalo <Largo y Ancho>")
    plt.savefig(name)


def prediction(df):
    """
    Realiza la predicción a partir de un dataframe
    :param df: DataFrame
    DataFrame que se utilizará para generar la predicción
    :return:
        - y_pred -Predicción de y
        - y_test -Tests de Y
    """
    x = df.drop("species", axis=1)
    y = df["species"]
    x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                        test_size=0.80,
                                                        random_state=0)
    clf = DecisionTreeClassifier()
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    return y_pred, y_test


def accuracy(y_test, y_pred):
    """

    :param y_test: Tests de y
    :param y_pred: Predicción de y
    :return: float Precisión de la predicción
    """
    return accuracy_score(y_test, y_pred)
