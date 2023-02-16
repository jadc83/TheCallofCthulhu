from muebles import mueble
from dado import dados
from character import *
from creature import *
from weapons import *

#### USO DEL CONSTRUCTOR ####
# Almacenar en una variable, subclase(Atributo, atributo....)
# nombre = subclase(atributo1, atributo2, atributo3....)


john = personaje("John Williams", dados(3,6), dados(3,6), dados(3,6), dados(3,6), "Vivo")
macario = personaje("Macario Smith", dados(3,6), dados(3,6), dados(3,6), dados(3,6), "Vivo")
cthulhu = primigenio("Cthulhu", dados(24,6), dados(50,6), dados(50,6), dados(19,6), dados(55,6), dados(600,6))
Nodens = diosmenor("Nodens", dados(20,6), dados(24,6), dados(24,6), dados(24,6), dados(24,6), dados(24,6))
cuchillo = armabasica("Cuchillo", "CC", 4, 2, 33, 10, 1, 5, "Si")
revolver = armaproyectil("Revolver", "Fuego", 50,  2, 10, 20,  3,  25, "Si", 20,  6,  6, True)
thompson = armaproyectil("Thompson", "Fuego", 15, 10,  5, 90, 20, 150, "Si", 45, 50, 50, True)
cajonera = mueble("Cajonera", "Pequeña mesita de noche completamente cubierta de polvo.", 100, [cuchillo, revolver, thompson])