import uuid


class PolvoCompacto:

    def __init__(self, tonalidades, nombre, marca, precio):
        self.tonalidades = tonalidades
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.codigo = uuid.uuid4()

    def __str__(self):
        return f"{self.codigo}--{self.nombre}--{self.tonalidades}--{self.marca}--{self.precio}"

    def __repr__(self):
        return str(self.codigo)

    def cumple_polvo(self, especificacion):
        dict_polvo = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_polvo or dict_polvo[k] != especificacion.get_value(k):
                return False
        return True
