import random

from Dominio.EspecificacionMaquillaje import EspecificacionMaquillaje
from Dominio.Inventario import Inventario
from Dominio.delineador import Delineador


def test_buscar_delineador():
    marcas = ['nyx', 'rimmel', 'maybelline']
    tipoDelineadores = {
        'nyx': ['rotulador', 'lapiz', 'liquido', 'polvo', 'gel'],
        'rimmel': ['rotulador', 'lapiz', 'liquido', 'polvo', 'gel'],
        'maybelline': ['rotulador', 'lapiz', 'liquido', 'polvo', 'gel']
    }
    inv = Inventario()
    for marca in marcas:
        for tipoDelineador in tipoDelineadores[marca]:
            inv.agregar_delineador(
                Delineador(tipoDelineador, 'fashion', 10000, marca)
            )
    especificacion = EspecificacionMaquillaje()
    especificacion.agregar_parametro('marca', 'nyx')
    for delineador in inv.buscar_delineador(especificacion):
        assert delineador is not None
    assert len(list(inv.buscar_delineador(especificacion))) >= 0


def test_fuzzing_buscar_delineador():
    nombres = ['36H', 'ucanbe', 'mizzu', 'essence']
    marcas = ['nyx', 'rimmel', 'maybelline']
    tipoDelineadores = {
        'nyx': ['rotulador', 'lapiz', 'liquido', 'polvo', 'gel'],
        'rimmel': ['rotulador', 'lapiz', 'liquido', 'polvo', 'gel'],
        'maybelline': ['rotulador', 'lapiz', 'liquido', 'polvo', 'gel']
    }
    precios = [10000, 20000, 30000, 40000, 50000]
    cantidad_delineadores = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_delineadores):
        nombre = random.choice(nombres)
        marca = random.choice(marcas)
        tipoDelineador = random.choice(tipoDelineadores[marca])
        precio = random.choice(precios)
        if i % 10 == 0:
            especificacion = EspecificacionMaquillaje()
            especificacion.agregar_parametro('tipoDelineador', tipoDelineador)
            especificacion.agregar_parametro('marca', marca)
            especificaciones.append(especificacion)
        l = Delineador(tipoDelineador, nombre, precio, marca)
        inventario.agregar_delineador(l)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_delineador(esp))) >= 0
        print('encontradas:')
        print(list(inventario.buscar_delineador(esp)))
    esp_fake = EspecificacionMaquillaje()
    esp_fake.agregar_parametro('solido', 'rosaida')
    print(inventario.delineadores)
    assert len(list(inventario.buscar_delineador(esp_fake))) == 0
    k = Delineador(tipoDelineador, nombre, precio, marca)
    inventario.agregar_delineador(k)
    try:
        inventario.agregar_delineador(k)
        assert False
    except Exception as ex:
        assert ex;


if __name__ == '__main__':
    test_fuzzing_buscar_delineador()
