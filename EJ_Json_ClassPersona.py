import datetime

class Personas (object):
    nombre = None
    apellido = None
    fecha_nac = None

    def __init__(self, nombre, apellido, fecha_nac):

        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac

    def serializacion (self):

        d = {
             "nombre": self.nombre,
             "apellido": self.apellido,
             "fdenac": str(self.fecha_nac)
            }

        return d

    def deserializacion (self, unaP):
        self.nombre = unaP["nombre"]
        self.apellido = unaP["apellido"]
        self.fecha_nac = datetime.datetime.strftime(unaP["fecha_nac"])

