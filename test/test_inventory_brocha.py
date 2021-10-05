import random

from Dominio.EspecificacionMaquillaje import EspecificacionMaquillaje
from Dominio.Inventario import Inventario
from Dominio.brocha import Brocha


def test_buscar_brocha():
    marcas = ['sigma', 'MAC', 'real techniques']
    tipoBrochas = {
        'sigma': ['plana', 'mofeta', 'cepillo'],
        'MAC': ['plana', 'mofeta', 'cepillo'],
        'real techniques': ['plana', 'mofeta', 'cepillo']
    }
    inv = Inventario()
    for marca in marcas:
        for tipoBrocha in tipoBrochas[marca]:
            inv.agregar_brocha(
                Brocha(tipoBrocha, 'brochas de rubor', 20000, marca)
            )
    especificacion = EspecificacionMaquillaje()
    especificacion.agregar_parametro('marca', 'sigma')
    for brocha in inv.buscar_brocha(especificacion):
        assert brocha is not None
    assert len(list(inv.buscar_brocha(especificacion))) >= 0


def test_fuzzing_buscar_brocha():
    nombres = ['brocha para polvos', 'brocha para blush', 'brocha para sombra', 'aplicacdor de esponja',
               'pincel angular', 'pincel para labios']
    marcas = ['sigma', 'MAC', 'real techniques']
    tipoBrochas = {
        'sigma': ['plana', 'mofeta', 'cepillo'],
        'MAC': ['plana', 'mofeta', 'cepillo'],
        'real techniques': ['plana', 'mofeta', 'cepillo']
    }
    precios = [5000, 10000, 15000, 20000, 25000, 40000, 50000]
    cantidad_brochas = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_brochas):
        nombre = random.choice(nombres)
        marca = random.choice(marcas)
        tipoBrocha = random.choice(tipoBrochas[marca])
        precio = random.choice(precios)
        if i % 10 == 0:
            especificacion = EspecificacionMaquillaje()
            especificacion.agregar_parametro('tipoBrocha', tipoBrocha)
            especificacion.agregar_parametro('marca', marca)
            especificaciones.append(especificacion)
        l = Brocha(tipoBrocha, nombre, precio, marca)
        inventario.agregar_brocha(l)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_brocha(esp))) >= 0
        print('encontradas:')
        print(list(inventario.buscar_brocha(esp)))
    esp_fake = EspecificacionMaquillaje()
    esp_fake.agregar_parametro('cuadrado', 'espinas')
    print(inventario.brochas)
    assert len(list(inventario.buscar_brocha(esp_fake))) == 0
    k = Brocha(tipoBrocha, nombre, precio, marca)
    inventario.agregar_brocha(k)
    try:
        inventario.agregar_brocha(k)
        assert False
    except Exception as ex:
        assert ex;


if __name__ == '__main__':
    test_fuzzing_buscar_brocha()
