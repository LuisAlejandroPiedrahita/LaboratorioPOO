import uuid


class Brocha:

    def __init__(self, tipoBrocha, nombre, precio, marca):
        self.tipoBrocha = tipoBrocha
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.codigo = uuid.uuid4()

    def __str__(self):
        return f"{self.codigo}--{self.nombre}--{self.tipoBrocha}--{self.marca}--{self.precio}"

    def __repr__(self):
        return str(self.codigo)

    def cumple_brocha(self, especificacion):
        dict_brocha = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_brocha or dict_brocha[k] != especificacion.get_value(k):
                return False
        return True
