import uuid


class Maquillaje:

    def __init__(self, nombre, precio, marca):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.codigo = uuid.uuid4()

    def __str__(self):
        return f"{self.codigo}--{self.nombre}--{self.marca}--{self.precio}"

    def __repr__(self):
        return str(self.codigo)

    def cumple_maquillaje(self, especificacion):
        dict_maquillaje = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_maquillaje or dict_maquillaje[k] != especificacion.get_value(k):
                return False
        return True
