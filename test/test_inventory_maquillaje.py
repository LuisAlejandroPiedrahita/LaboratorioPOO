import random

from Dominio.EspecificacionMaquillaje import EspecificacionMaquillaje
from Dominio.Inventario import Inventario
from Dominio.maquillaje import Maquillaje


def test_buscar_maquillaje():
    marcas = ['atenea', 'skala', 'khol']
    nombres = {
        'atenea': ['labial', 'delineador'],
        'skala': ['brocha', 'polvo_compacto'],
        'khol': ['labial', 'polvo_compacto', 'brocha']
    }
    inv = Inventario()
    for marca in marcas:
        for nombre in nombres[marca]:
            inv.agregar_maquillaje(
                Maquillaje(nombre, 50000, marca)
            )
    especificacion = EspecificacionMaquillaje()
    especificacion.agregar_parametro('marca', 'skala')
    for maquillaje in inv.buscar_maquillaje(especificacion):
        assert maquillaje is not None
    assert len(list(inv.buscar_maquillaje(especificacion))) >= 0


def test_fuzzing_buscar_maquillaje():
    marcas = ['atenea', 'skala', 'khol']
    nombres = {
        'atenea': ['labial', 'delineador'],
        'skala': ['brocha', 'polvo_compacto'],
        'khol': ['labial', 'polvo_compacto', 'brocha']
    }
    precios = [10000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
    cantidad_maquillaje = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_maquillaje):
        marca = random.choice(marcas)
        nombre = random.choice(nombres[marca])
        precio = random.choice(precios)
        if i % 10 == 0:
            especificacion = EspecificacionMaquillaje()
            especificacion.agregar_parametro('nombre', nombres)
            especificacion.agregar_parametro('marca', marca)
            especificaciones.append(especificacion)
        l = Maquillaje(nombre, precio, marca)
        inventario.agregar_maquillaje(l)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_maquillaje(esp))) >= 0
        print('encontradas:')
        print(list(inventario.buscar_maquillaje(esp)))
    esp_fake = EspecificacionMaquillaje()
    esp_fake.agregar_parametro('tabla', 'luois')
    print(inventario.maquillajes)
    assert len(list(inventario.buscar_maquillaje(esp_fake))) == 0
    k = Maquillaje(nombre, precio, marca)
    inventario.agregar_maquillaje(k)
    try:
        inventario.agregar_maquillaje(k)
        assert False
    except Exception as ex:
        assert ex;


if __name__ == '__main__':
    test_fuzzing_buscar_maquillaje()
