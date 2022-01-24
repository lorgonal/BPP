class Car:
    """
    Clase que define un coche
    """
    def __init__(self, brand, model):
        """
        Instancia un coche

        :param brand: str
        Marca del coche

        :param model: str
        Modelo del coche
        """
        self.started = False
        self.brand = brand
        self.model = model

    def start_engine(self):
        """
        Arranca el coche

        :return: None
        """
        print('brum brum')
        self.started = True

    def status(self):
        """
        Indica si el coche está arrancado

        :return: None
        """
        if self.started:
            print('Coche arrancado')
        else:
            print('Coche parado')

    def print_car(self):
        """
        Escribe los detalles del coche

        :return:None
        """
        print(f'Marca: {self.brand}\nModelo: {self.model}\n')


if __name__ == '__main__':

    my_car = Car('BMW', 'X3')
    my_car.start_engine()
    my_car.status()
    my_car.print_car()

