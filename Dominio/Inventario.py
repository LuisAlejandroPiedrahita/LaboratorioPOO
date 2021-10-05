from Dominio.EspecificacionMaquillaje import EspecificacionMaquillaje
from Dominio.labial import Labial
from Dominio.brocha import Brocha
from Dominio.maquillaje import Maquillaje
from Dominio.delineador import Delineador
from Dominio.polvoCompacto import PolvoCompacto


class Inventario:

    def __init__(self):
        self.labiales = []
        self.brochas = []
        self.delineadores = []
        self.maquillajes = []
        self.polvos = []

    def agregar_labial(self, labial):
        if type(labial) == Labial:
            espec = EspecificacionMaquillaje()
            espec.agregar_parametro('codigo', labial.codigo)
            if len(list(self.buscar_Labial(espec))) == 0:
                self.labiales.append(labial)
            else:
                raise Exception('Labial repetido')

    def buscar_Labial(self, especificacion):
        for g in self.labiales:
            if g.cumple_labial(especificacion):
                yield g

    def agregar_brocha(self, brocha):
        if type(brocha) == Brocha:
            espec = EspecificacionMaquillaje()
            espec.agregar_parametro('codigo', brocha.codigo)
            if len(list(self.buscar_brocha(espec))) == 0:
                self.brochas.append(brocha)
            else:
                raise Exception('Brocha repetida')

    def buscar_brocha(self, especificacion):
        for g in self.brochas:
            if g.cumple_brocha(especificacion):
                yield g

    def agregar_delineador(self, delineador):
        if type(delineador) == Delineador:
            espec = EspecificacionMaquillaje()
            espec.agregar_parametro('codigo', delineador.codigo)
            if len(list(self.buscar_delineador(espec))) == 0:
                self.delineadores.append(delineador)
            else:
                raise Exception('Delineador repetido')

    def buscar_delineador(self, especificacion):
        for g in self.delineadores:
            if g.cumple_delineador(especificacion):
                yield g

    def agregar_polvo(self, polvoCompacto):
        if type(polvoCompacto) == PolvoCompacto:
            espec = EspecificacionMaquillaje()
            espec.agregar_parametro('codigo', polvoCompacto.codigo)
            if len(list(self.buscar_polvo(espec))) == 0:
                self.polvos.append(polvoCompacto)
            else:
                raise Exception('Polvo Compacto repetido')

    def buscar_polvo(self, especificacion):
        for g in self.polvos:
            if g.cumple_polvo(especificacion):
                yield g

    def agregar_maquillaje(self, maquillaje):
        if type(maquillaje) == Maquillaje:
            espec = EspecificacionMaquillaje()
            espec.agregar_parametro('codigo', maquillaje.codigo)
            if len(list(self.buscar_maquillaje(espec))) == 0:
                self.maquillajes.append(maquillaje)
            else:
                raise Exception('Maquillaje repetido')

    def buscar_maquillaje(self, especificacion):
        for g in self.maquillajes:
            if g.cumple_maquillaje(especificacion):
                yield g
