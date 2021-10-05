import random

from Dominio.EspecificacionMaquillaje import EspecificacionMaquillaje
from Dominio.Inventario import Inventario
from Dominio.labial import Labial


def test_buscar_labial():
    marcas = ['zara', 'rimmel', 'nyx']
    colores = {
        'zara': ['rojo', 'cafe', 'rosa', 'azul'],
        'rimmel': ['rojo', 'cafe', 'morado', 'rosa'],
        'nyx': ['rojo', 'mate', 'cafe', 'rosa', 'morado', 'azul']
    }
    inv = Inventario()
    for marca in marcas:
        for color in colores[marca]:
            inv.agregar_labial(
                Labial(color, "diva", marca, 1000000)
            )
    especificacion = EspecificacionMaquillaje()
    especificacion.agregar_parametro('marca', 'nyx')
    for labial in inv.buscar_Labial(especificacion):
        assert labial is not None
    assert len(list(inv.buscar_Labial(especificacion))) > 0


def test_fuzzing_buscar_labial():
    nombres = ['diva', 'baby doll', 'chili']
    marcas = ['zara', 'rimmel', 'nyx']
    colores = {
        'zara': ['rojo', 'cafe', 'rosa', 'azul'],
        'rimmel': ['rojo', 'cafe', 'morado', 'rosa', 'naranja'],
        'nyx': ['rojo', 'mate', 'cafe', 'rosa', 'morado', 'azul']
    }
    precios = [50000, 60000, 70000, 100000, 150000, 250000, 300000, 400000, 500000]
    cantidad_labiales = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_labiales):
        nombre = random.choice(nombres)
        marca = random.choice(marcas)
        color = random.choice(colores[marca])
        precio = random.choice(precios)
        if i % 10 == 0:
            especificacion = EspecificacionMaquillaje()
            especificacion.agregar_parametro('color', color)
            especificacion.agregar_parametro('marca', marca)
            especificaciones.append(especificacion)
        l = Labial(color, nombre, marca, precio)
        inventario.agregar_labial(l)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_Labial(esp))) >= 0
        print('encontradas:')
        print(list(inventario.buscar_Labial(esp)))
    esp_fake = EspecificacionMaquillaje()
    esp_fake.agregar_parametro('hidratante', 'morado')
    print(inventario.labiales)
    assert len(list(inventario.buscar_Labial(esp_fake))) == 0
    k = Labial(color, nombre, marca, precio)
    inventario.agregar_labial(k)
    try:
        inventario.agregar_labial(k)
        assert False
    except Exception as ex:
        assert ex;


if __name__ == '__main__':
    test_fuzzing_buscar_labial()
