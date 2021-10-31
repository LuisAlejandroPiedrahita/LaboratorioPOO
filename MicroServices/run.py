import json
import waitress
import falcon
from falcon import API

from Infranstructura.PersistenciaTienda import PersistenciaTienda

class maquillaje():

        def on_get(self, req, resp, codigo):

                bd = PersistenciaTienda()
                gui = bd.load_json_maquillaje(codigo + '.jsonMaquillaje')
                resp.body = json.dumps(gui.__dict__)
                resp.status = falcon.HTTP_OK

def iniciar() -> API:

        api = API()
        api.add_route("7maquillaje/{codigo}",maquillaje())
        return api

app = iniciar()

if __name__ == '__main__':

        waitress.serve(app,port = 2020, url_scheme = 'http')
