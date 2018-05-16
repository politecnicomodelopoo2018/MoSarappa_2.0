from Ej8ClassTrabajadores import  trabajador

class programa (object):

    nombrePrograma = None
    OperadorTecnico = None
    Categoria = None



    def __init__(self, nombrePrograma, OperadorTecnico, Categoria,horario):

        self.nombrePrograma = nombrePrograma
        self.OperadorTecnico = OperadorTecnico
        self.Categoria = Categoria
        self.horario = horario



        self.ListaConductoresProg = []



    def AgregarConductores (self, unConductor):

        self.ListaConductoresProg.append(unConductor)

    def AgregarOperador (self, unOperador):

        self.OperadorTecnico = unOperador



class programa_musica (programa):

    nombreMusicalizador = None
    estilosDeMusica = None

    def __init__(self, nombrePrograma, OperadorTecnico, Categoria,nombreMusicalizador,estilosDeMusica ):

        programa.__init__(self,  nombrePrograma, OperadorTecnico, Categoria)

        self.nombreMusicalizador = nombreMusicalizador
        self.estilosDeMusica = estilosDeMusica

    def AgregarMusicalizador(self, unMusicalizador):
        self.nombrePrograma = unMusicalizador



