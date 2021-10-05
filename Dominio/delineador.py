import uuid


class Delineador:

    def __init__(self, tipoDelineador, nombre, precio, marca):
        self.tipoDelineador = tipoDelineador
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.codigo = uuid.uuid4()

    def __str__(self):
        return f"{self.codigo}--{self.nombre}--{self.tipoDelineador}--{self.marca}--{self.precio}"

    def __repr__(self):
        return str(self.codigo)

    def cumple_delineador(self, especificacion):
        dict_delineador = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_delineador or dict_delineador[k] != especificacion.get_value(k):
                return False
        return True
