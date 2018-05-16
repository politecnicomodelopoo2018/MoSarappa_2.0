class radio (object):

    nombrePrograma = None


    def __init__(self, nombrePrograma):

        self.nombrePrograma = nombrePrograma

        self.Lista_Programas = []


    def AgregarPrograma (self, unPrograma):

        for item in self.Lista_Programas:
            if item.horario == unPrograma.horario:
                return False

        self.Lista_Programas.append(unPrograma)








