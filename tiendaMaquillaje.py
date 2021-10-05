from Dominio.Inventario import Inventario
from Dominio.maquillaje import Maquillaje
from Dominio.labial import Labial
from Dominio.brocha import Brocha
from Dominio.delineador import Delineador
from Dominio.polvoCompacto import PolvoCompacto
from Infranstructura.PersistenciaTienda import PersistenciaTienda

inventario = Inventario()
import random
import os

if __name__ == '__main__':
    # ----------------BASE DE DATOS-----------------------
    saver = PersistenciaTienda()
    saver.connect()
    # ----------------------------------------------------

    # -------------------MENUS----------------------------
    menuPrincipal = True
    menuAgregar = True
    menuGuardarMaquillaje = True
    menuGuardarLabial = True
    menuGuardarBrocha = True
    menuGuardarDelineador = True
    menuGuardarPolvo = True
    menuBuscar = True
    menuVender = True
    # ----------------------------------------------------

    while menuPrincipal:
        print("-+-"*20)
        print("Menu Principal: \n"
              "1- Agregar Maquillaje \n"
              "2- Buscar Maquillaje \n"
              "3- Vender Maquillaje \n"
              "4- Salir \n")
        menuPrincipal = int(input("Ingrese el numero de la opcion: "))

        # --------------- OPCION 1 PARA AGREGAR LOS PRODUCTOS ----------------------
        if menuPrincipal == 1:
            while menuAgregar:
                print("-+-"*20)
                print("Menu De Agregar Maquillaje \n"
                      "1- Agregar Maquillaje (En esta opcion se puede agregar cualquier tipo de producto)\n"
                      "2- Agregar Labial \n"
                      "3- Agregar Brocha \n"
                      "4- Agregar Delineador \n"
                      "5- Agregar PolvoCompacto \n"
                      "6- Volver \n")
                menuAgregar = int(input("Ingrese la opcion que quiere: "))

                if menuAgregar == 1:
                    marcas = ['atenea', 'skala', 'khol']
                    nombres = {
                        'atenea': ['labial', 'delineador'],
                        'skala': ['brocha', 'polvo_compacto'],
                        'khol': ['labial', 'polvo_compacto', 'brocha']
                    }
                    precios = [10000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
                    marca = random.choice(marcas)
                    nombre = random.choice(nombres[marca])
                    precio = random.choice(precios)
                    maquillaje = Maquillaje(nombre, precio, marca)
                    while menuGuardarMaquillaje:
                        print("-+-"*20)
                        print("En que tipo de almacenamiento quiere guardar los datos \n"
                              "1- Datos Json \n"
                              "2- Base de datos \n"
                              "3- Volver \n")
                        menuGuardarMaquillaje = int(input("Ingrese el numero de la opcion: "))
                        if menuGuardarMaquillaje == 1:
                            PersistenciaTienda.save_json_maquillaje(maquillaje)
                            inventario = Inventario()
                            inventario_json = Inventario()
                            for file in os.listdir("./files/maquillaje"):
                                if '.json' in file:
                                    inventario_json.agregar_maquillaje(PersistenciaTienda.load_json_maquillaje(file))
                            for maquillaje in inventario.maquillajes:
                                PersistenciaTienda.save_json_maquillaje(maquillaje)
                            break
                        elif menuGuardarMaquillaje == 2:
                            saver.guardar_maquillaje(maquillaje)
                            break
                        else:
                            menuGuardarMaquillaje = False

                elif menuAgregar == 2:
                    nombres = ['diva', 'baby_doll', 'chili']
                    marcas = ['zara', 'rimmel', 'nyx']
                    colores = {
                        'zara': ['rojo', 'cafe', 'rosa', 'azul'],
                        'rimmel': ['rojo', 'cafe', 'morado', 'rosa', 'naranja'],
                        'nyx': ['rojo', 'mate', 'cafe', 'rosa', 'morado', 'azul']}
                    precios = [50000, 60000, 70000, 100000, 150000, 250000, 300000, 400000, 500000]
                    nombre = random.choice(nombres)
                    marca = random.choice(marcas)
                    color = random.choice(colores[marca])
                    precio = random.choice(precios)
                    labial = Labial(color, nombre, marca, precio)
                    while menuGuardarLabial:
                        print("-+-"*20)
                        print("En que tipo de almacenamiento quiere guardar los datos \n"
                              "1- Datos Json \n"
                              "2- Base de datos \n"
                              "3- Volver \n")
                        menuGuardarLabial = int(input("Ingrese el numero de la opcion: "))
                        if menuGuardarLabial == 1:
                            PersistenciaTienda.save_json_labial(labial)
                            inventario = Inventario()
                            inventario_json = Inventario()
                            for file in os.listdir("./files/labial"):
                                if '.json' in file:
                                    inventario_json.agregar_labial(PersistenciaTienda.load_json_labial(file))
                            for labial in inventario.labiales:
                                PersistenciaTienda.save_json_labial(labial)
                            break
                        elif menuGuardarLabial == 2:
                            saver.guardar_labial(labial)
                            break
                        else:
                            menuGuardarLabial = False

                elif menuAgregar == 3:
                    nombres = ['brocha_para_polvos', 'brocha_para_blush', 'brocha_para_sombra', 'aplicacdor_de_esponja',
                               'pincel_angular', 'pincel_para_labios']
                    marcas = ['sigma', 'MAC', 'real_techniques']
                    tipoBrochas = {
                        'sigma': ['plana', 'mofeta', 'cepillo'],
                        'MAC': ['plana', 'mofeta', 'cepillo'],
                        'real_techniques': ['plana', 'mofeta', 'cepillo']
                    }
                    precios = [5000, 10000, 15000, 20000, 25000, 40000, 50000]
                    nombre = random.choice(nombres)
                    marca = random.choice(marcas)
                    tipoBrocha = random.choice(tipoBrochas[marca])
                    precio = random.choice(precios)
                    brocha = Brocha(tipoBrocha, nombre, precio, marca)
                    inventario = Inventario()
                    inventario_json = Inventario()
                    while menuGuardarBrocha:
                        print("-+-"*20)
                        print("En que tipo de almacenamiento quiere guardar los datos \n"
                              "1- Datos Json \n"
                              "2- Base de datos \n"
                              "3- Volver \n")
                        menuGuardarBrocha = int(input("Ingrese el numero de la opcion: "))
                        if menuGuardarBrocha == 1:
                            PersistenciaTienda.save_json_brocha(brocha)
                            for file in os.listdir("./files/brocha"):
                                if '.json' in file:
                                    inventario_json.agregar_brocha(PersistenciaTienda.load_json_brocha(file))
                            for brocha in inventario.brochas:
                                PersistenciaTienda.save_json_brocha(brocha)
                            break
                        elif menuGuardarBrocha == 2:
                            saver.guardar_brocha(brocha)
                            break
                        else:
                            menuGuardarBrocha = False

                elif menuAgregar == 4:
                    nombres = ['36H', 'ucanbe', 'mizzu', 'essence']
                    marcas = ['nyx', 'rimmel', 'maybelline']
                    tipoDelineadores = {
                        'nyx': ['rotulador', 'lapiz', 'liquido', 'polvo', 'gel'],
                        'rimmel': ['rotulador', 'lapiz', 'liquido', 'polvo', 'gel'],
                        'maybelline': ['rotulador', 'lapiz', 'liquido', 'polvo', 'gel']
                    }
                    precios = [10000, 20000, 30000, 40000, 50000]
                    nombre = random.choice(nombres)
                    marca = random.choice(marcas)
                    tipoDelineador = random.choice(tipoDelineadores[marca])
                    precio = random.choice(precios)
                    delineador = Delineador(tipoDelineador, nombre, precio, marca)
                    while menuGuardarDelineador:
                        print("-+-"*20)
                        print("En que tipo de almacenamiento quiere guardar los datos \n"
                              "1- Datos Json \n"
                              "2- Base de datos \n"
                              "3- Volver \n")
                        menuGuardarDelineador = int(input("Ingrese el numero de la opcion: "))
                        if menuGuardarDelineador == 1:
                            PersistenciaTienda.save_json_delineador(delineador)
                            inventario = Inventario()
                            inventario_json = Inventario()
                            for file in os.listdir("./files/delineador"):
                                if '.json' in file:
                                    inventario_json.agregar_delineador(PersistenciaTienda.load_json_delineador(file))
                            for delineador in inventario.delineadores:
                                PersistenciaTienda.save_json_delineador(delineador)
                            break
                        elif menuGuardarDelineador == 2:
                            saver.guardar_delineador(delineador)
                            break
                        else:
                            menuGuardarDelineador = False

                elif menuAgregar == 5:
                    nombres = ['marcelle', 'touch', 'love', 'mineral']
                    marcas = ['vogue', 'pure', 'maybelline']
                    tonalidades = {
                        'vogue': ['natural', 'beige', 'arena', 'almendra', 'aceituna'],
                        'pure': ['natural', 'almendra', 'arena', 'aceituna', 'canela'],
                        'maybelline': ['moka', 'tostado', 'canela', 'almendra', 'beige']
                    }
                    precios = [20000, 30000, 50000, 60000]
                    nombre = random.choice(nombres)
                    marca = random.choice(marcas)
                    tonalidad = random.choice(tonalidades[marca])
                    precio = random.choice(precios)
                    polvoCompacto = PolvoCompacto(tonalidad, nombre, precio, marca)
                    while menuGuardarPolvo:
                        print("-+-"*20)
                        print("En que tipo de almacenamiento quiere guardar los datos \n"
                              "1- Datos Json \n"
                              "2- Base de datos \n"
                              "3- Volver \n")
                        menuGuardarPolvo = int(input("Ingrese el numero de la opcion: "))
                        if menuGuardarPolvo == 1:
                            PersistenciaTienda.save_json_polvoCompacto(polvoCompacto)
                            inventario = Inventario()
                            inventario_json = Inventario()
                            for file in os.listdir("./files/polvoCompacto"):
                                if '.json' in file:
                                    inventario_json.agregar_polvo(PersistenciaTienda.load_json_polvoCompacto(file))
                            for polvoCompacto in inventario.polvos:
                                PersistenciaTienda.save_json_polvoCompacto(polvoCompacto)
                            break
                        elif menuGuardarPolvo == 2:
                            saver.guardar_polvoCompacto(polvoCompacto)
                            break
                        else:
                            menuGuardarPolvo = False

                elif menuAgregar == 6:
                    menuAgregar = False
                else:
                    print("Ingrese algun numero del menu")
                    print("-+-"*20)

        # --------------------------------------------------------------------------

        # --------------- OPCION 2 PARA BUSCAR LOS PRODUCTOS -----------------------
        elif menuPrincipal == 2:
            while menuBuscar:
                print("-+-"*20)
                print("Menu De Buscar Maquillaje \n"
                      "1- Buscar Maquillaje (En esta opcion se puede agregar cualquier tipo de producto)\n"
                      "2- Buscar Labial \n"
                      "3- Buscar Brocha \n"
                      "4- Buscar Delineador \n"
                      "5- Buscar PolvoCompacto \n"
                      "6- Volver \n")
                menuBuscar = int(input("Ingrese la opcion que quiere buscar: "))

                if menuBuscar == 1:
                    print("-+-"*20)
                    print("Se encontro un maquillaje ")
                elif menuBuscar == 2:
                    print("-+-"*20)
                    print("Se encontro un Labial ")
                elif menuBuscar == 3:
                    print("-+-"*20)
                    print("Se encontro una Brocha ")
                elif menuBuscar == 4:
                    print("-+-"*20)
                    print("Se encontro un Delineador ")
                elif menuBuscar == 5:
                    print("-+-"*20)
                    print("Se encontro un PolvoCompacto ")
                elif menuBuscar == 6:
                    menuBuscar = False
                else:
                    print("Ingrese algun numero del menu")
                    print("-+-"*20)

        # --------------------------------------------------------------------------

        # --------------- OPCION 3 PARA VENDER LOS PRODUCTOS -----------------------
        elif menuPrincipal == 3:
            while menuVender:
                print("-+-"*20)
                print("Menu De Vender Maquillaje \n"
                      "1- Vender Maquillaje (En esta opcion se puede agregar cualquier tipo de producto)\n"
                      "2- Vender Labial \n"
                      "3- Vender Brocha \n"
                      "4- Vender Delineador \n"
                      "5- Vender PolvoCompacto \n"
                      "6- Volver \n")
                menuVender = int(input("Ingrese la opcion del producto que quiere vender: "))

                if menuVender == 1:
                    print("-+-"*20)
                    print("Se vendio un Maquillaje ")
                elif menuVender == 2:
                    print("-+-"*20)
                    print("Se vendio un Labial ")
                elif menuVender == 3:
                    print("-+-"*20)
                    print("Se vendio una Brocha ")
                elif menuVender == 4:
                    print("-+-"*20)
                    print("Se vendio un Delineador ")
                elif menuVender == 5:
                    print("-+-"*20)
                    print("Se vendio un PolvoCompacto ")
                elif menuVender == 6:
                    menuVender = False
                else:
                    print("Ingrese algun numero del menu")
                    print("-+-"*20)

        # --------------------------------------------------------------------------

        # --------------- OPCION 4 PARA SALIR DEL PROGRAMA -------------------------
        elif menuPrincipal == 4:
            menuPrincipal = False

        else:
            print("Ingrese algun numero del menu")
            print("-+-"*20)

