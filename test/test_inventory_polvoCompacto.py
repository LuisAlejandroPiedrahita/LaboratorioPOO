import random

from Dominio.EspecificacionMaquillaje import EspecificacionMaquillaje
from Dominio.Inventario import Inventario
from Dominio.polvoCompacto import PolvoCompacto


def test_buscar_polvo():
    marcas = ['vogue', 'pure', 'maybelline']
    tonalidades = {
        'vogue': ['natural', 'beige', 'arena','almendra','aceituna'],
        'pure': ['natural', 'almendra', 'arena','aceituna','canela'],
        'maybelline': ['moka', 'tostado', 'canela','almendra','beige']
    }
    inv = Inventario()
    for marca in marcas:
        for tonalidad in tonalidades[marca]:
            inv.agregar_polvo(
                PolvoCompacto(tonalidad,'samy',marca,50000)
            )
    especificacion = EspecificacionMaquillaje()
    especificacion.agregar_parametro('marca', 'pure')
    for polvo in inv.buscar_polvo(especificacion):
        assert polvo is not None
    assert len(list(inv.buscar_polvo(especificacion))) >= 0


def test_fuzzing_buscar_polvo():
    nombres = ['marcelle','touch','love','mineral']
    marcas = ['vogue', 'pure', 'maybelline']
    tonalidades = {
        'vogue': ['natural', 'beige', 'arena','almendra','aceituna'],
        'pure': ['natural', 'almendra', 'arena','aceituna','canela'],
        'maybelline': ['moka', 'tostado', 'canela','almendra','beige']
    }
    precios = [20000,30000,50000,60000]
    cantidad_polvos = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_polvos):
        nombre = random.choice(nombres)
        marca = random.choice(marcas)
        tonalidad = random.choice(tonalidades[marca])
        precio = random.choice(precios)
        if i % 10 == 0:
            especificacion = EspecificacionMaquillaje()
            especificacion.agregar_parametro('tonalidad', tonalidades)
            especificacion.agregar_parametro('marca', marca)
            especificaciones.append(especificacion)
        l = PolvoCompacto(tonalidad,nombre,marca,precio)
        inventario.agregar_polvo(l)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_polvo(esp))) >= 0
        print('encontradas:')
        print(list(inventario.buscar_polvo(esp)))
    esp_fake = EspecificacionMaquillaje()
    esp_fake.agregar_parametro('cafe', 'stellar')
    print(inventario.polvos)
    assert len(list(inventario.buscar_polvo(esp_fake))) == 0
    k = PolvoCompacto(tonalidad,nombre,marca,precio)
    inventario.agregar_polvo(k)
    try:
        inventario.agregar_polvo(k)
        assert False
    except Exception as ex:
        assert ex;


if __name__ == '__main__':
    test_fuzzing_buscar_polvo()
