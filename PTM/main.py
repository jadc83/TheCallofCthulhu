
from dado import dados
from character import *
from weapons import *

#### USO DEL CONSTRUCTOR ####
# Almacenar en una variable, subclase(Atributo, atributo....)
# nombre = subclase(atributo1, atributo2, atributo3....)

anna = personaje("Anna Williams", dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6))
sebastian = policia("Sebastian Martinez", dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), 12, 4)
john = investigador("John Williams", dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), 10, 6)
jacinto = escritor("Jacinto Perez",  dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), 10)
cuchillo = armabasica("Cuchillo", "CC", 4, 2, 33, 10, 1, 5, "Si")
revolver = armaproyectil("Revolver", "Fuego", 12, 2, 10, 20, 3, 25, "Si", 20, 6, 6)

