from pydantic import BaseModel


class IrisClass(BaseModel):
    """
    Clase con los datos del Iris

    Atributos:
    ==========
    sepal_length: float Longitud del sépalo
    sepal_width: float Grosor del sépalo
    petal_length: float Longitud del pétalo
    petal_width: float Grosor del pétalo
    species: str Especie
    """
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str

