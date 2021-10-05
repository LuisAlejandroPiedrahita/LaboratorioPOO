import uuid


class Labial:

    def __init__(self, color, nombre, marca, precio):
        self.color = color
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.codigo = uuid.uuid4()

    def __str__(self):
        return f"{self.codigo}--{self.color}--{self.nombre}--{self.marca}--{self.precio}"

    def __repr__(self):
        return str(self.codigo)

    def cumple_labial(self, especificacion):
        dict_labial = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_labial or dict_labial[k] != especificacion.get_value(k):
                return False
        return True
