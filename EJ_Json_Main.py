import  json
from EJ_Json_ClassPersona import Personas

a1 = Personas("Carlos", "Luko", "2018/09/10")


ListaPersona = []

ListaPersona.append(a1)

d= {"personas": []}

for item in ListaPersona:

    d["persona"].append(item.serializacion())

f = open ("misPersonas.json", "w")
f.write(json.dumps(d))
f.close()

f = open ("misPersonas.json", "r")
d = json.loads (f.read())

for item in d["personas"] :

    unaPersona = Personas()
    unaPersona.deserializacion(item)
    ListaPersona.append (unaPersona)

f.close ()