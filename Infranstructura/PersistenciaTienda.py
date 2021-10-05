import sqlite3

import jsonpickle

from Dominio.brocha import Brocha
from Dominio.delineador import Delineador
from Dominio.labial import Labial
from Dominio.maquillaje import Maquillaje
from Dominio.polvoCompacto import PolvoCompacto


class PersistenciaTienda:

    def __init__(self):
        self.con = sqlite3.connect("Paris_Fashion.sqlite")

    def connect(self):
        self.__crear_tabla_labial()
        self.__crear_tabla_brocha()
        self.__crear_tabla_delineador()
        self.__crear_tabla_polvoCompacto()
        self.__crear_tabla_maquillaje()

    def __crear_tabla_labial(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE LABIAL(codigo text primary key, nombre text," \
                    " marca text, color text, precio float)"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_labial(self, labial: Labial):
        cursor = self.con.cursor()
        query = "insert into LABIAL(codigo , nombre ," \
                " marca , color ,precio ) values(" \
                f" ?,?,?,?,?)"
        cursor.execute(query, (str(labial.codigo), labial.nombre, labial.marca,
                               labial.color, labial.precio))
        self.con.commit()

    @classmethod
    def save_json_labial(cls, labial):
        text_open = open("files/labial/" + str(labial.codigo) + '.json', mode='w')
        json_gui = jsonpickle.encode(labial)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_labial(cls, file_name):
        text_open = open("files/labial/" + file_name, mode='r')
        json_gui = text_open.readline()
        labial = jsonpickle.decode(json_gui)
        text_open.close()
        return labial

    def __crear_tabla_brocha(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE BROCHA(codigo text primary key, nombre text," \
                    " marca text, tipoBrocha text, precio float)"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_brocha(self, brocha: Brocha):
        cursor = self.con.cursor()
        query = "insert into BROCHA(codigo , nombre ," \
                " marca , tipoBrocha ,precio ) values(" \
                f" ?,?,?,?,?)"
        cursor.execute(query, (str(brocha.codigo), brocha.nombre, brocha.marca,
                               brocha.tipoBrocha, brocha.precio))
        self.con.commit()

    @classmethod
    def save_json_brocha(cls, brocha):
        text_open = open("files/brocha/" + str(brocha.codigo) + '.json', mode='w')
        json_gui = jsonpickle.encode(brocha)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_brocha(cls, file_name):
        text_open = open("files/brocha/" + file_name, mode='r')
        json_gui = text_open.readline()
        brocha = jsonpickle.decode(json_gui)
        text_open.close()
        return brocha

    def __crear_tabla_delineador(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE DELINEADOR(codigo text primary key, nombre text," \
                    " marca text, tipoDelineador text, precio float)"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_delineador(self, delineador: Delineador):
        cursor = self.con.cursor()
        query = "insert into DELINEADOR(codigo , nombre ," \
                " marca , tipoDelineador ,precio ) values(" \
                f" ?,?,?,?,?)"
        cursor.execute(query, (str(delineador.codigo), delineador.nombre, delineador.marca,
                               delineador.tipoDelineador, delineador.precio))
        self.con.commit()

    @classmethod
    def save_json_delineador(cls, delineador):
        text_open = open("files/delineador/" + str(delineador.codigo) + '.json', mode='w')
        json_gui = jsonpickle.encode(delineador)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_delineador(cls, file_name):
        text_open = open("files/delineador/" + file_name, mode='r')
        json_gui = text_open.readline()
        delineador = jsonpickle.decode(json_gui)
        text_open.close()
        return delineador

    def __crear_tabla_polvoCompacto(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE POLVOCOMPACTO(codigo text primary key, nombre text," \
                    " marca text, tonalidades text, precio float)"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_polvoCompacto(self, polvoCompacto: PolvoCompacto):
        cursor = self.con.cursor()
        query = "insert into POLVOCOMPACTO(codigo , nombre ," \
                " marca , tonalidades ,precio ) values(" \
                f" ?,?,?,?,?)"
        cursor.execute(query, (str(polvoCompacto.codigo), polvoCompacto.nombre, polvoCompacto.marca,
                               polvoCompacto.tonalidades, polvoCompacto.precio))
        self.con.commit()

    @classmethod
    def save_json_polvoCompacto(cls, polvoCompacto):
        text_open = open("files/polvoCompacto/" + str(polvoCompacto.codigo) + '.json', mode='w')
        json_gui = jsonpickle.encode(polvoCompacto)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_polvoCompacto(cls, file_name):
        text_open = open("files/polvoCompacto/" + file_name, mode='r')
        json_gui = text_open.readline()
        polvoCompacto = jsonpickle.decode(json_gui)
        text_open.close()
        return polvoCompacto

    def __crear_tabla_maquillaje(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE MAQUILLAJE(codigo text primary key, nombre text," \
                    " marca text, precio float)"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_maquillaje(self, maquillaje: Maquillaje):
        cursor = self.con.cursor()
        query = "insert into MAQUILLAJE(codigo , nombre ," \
                " marca ,precio ) values(" \
                f" ?,?,?,?)"
        cursor.execute(query, (str(maquillaje.codigo), maquillaje.nombre, maquillaje.marca,
                               maquillaje.precio))
        self.con.commit()

    @classmethod
    def save_json_maquillaje(cls, maquillaje):
        text_open = open("files/maquillaje/" + str(maquillaje.codigo) + '.json', mode='w')
        json_gui = jsonpickle.encode(maquillaje)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_maquillaje(cls, file_name):
        text_open = open("files/maquillaje/" + file_name, mode='r')
        json_gui = text_open.readline()
        maquillaje = jsonpickle.decode(json_gui)
        text_open.close()
        return maquillaje
