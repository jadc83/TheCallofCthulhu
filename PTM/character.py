from dado import dados
class personaje:
    
    def __init__(self, nombre, fuerza, constitucion, tamaño, destreza, apariencia, inteligencia, educacion, poder):
        """Metodo constructor."""
        self.nombre = nombre
        self.FUE = fuerza
        self.CON = constitucion
        self.TAM = tamaño
        self.DES = destreza
        self.APA = apariencia
        self.INT = inteligencia
        self.EDU = educacion + 3
        self.POD = poder
        self.SUE = self.POD * 5
        self.HP = ( self.TAM + self.CON ) / 2
        self.MP = self.POD

    def atributos(self):
        """Muestra los atributos"""
        print(".Nombre:", self.nombre)
        print(".FUE:", self.FUE)
        print(".CON:", self.CON)
        print(".TAM", self.TAM)
        print(".DES:", self.DES)
        print(".APA:", self.APA)
        print(".INT:", self.INT)
        print(".EDU:", self.EDU)
        print(".POD:", self.POD)
        print(".SUE", self.SUE)
        print(".HP", self.HP)
        print(".MP", self.MP)
        
######METODOS DE PERSONAJE VAN AQUI#############
            

class investigador(personaje):
    
    def __init__(self, nombre, fuerza, constitucion, tamaño, destreza, apariencia, inteligencia, educacion, poder, revolver, navaja):
        super().__init__(nombre, fuerza, constitucion, tamaño, destreza, apariencia, inteligencia, educacion, poder)
        self.revolver = revolver
        self.navaja = navaja
        
########METODOS DE INVESTIGADOR VAN AQUI#############
    
    def atributos(self):
        super().atributos()
        print(".Revolver", self.revolver)
        print(".Navaja", self.navaja)

class policia(personaje):
    
    def __init__(self, nombre, fuerza, constitucion, tamaño, destreza, apariencia, inteligencia, educacion, poder, revolver, porra):
        super().__init__(nombre, fuerza, constitucion, tamaño, destreza, apariencia, inteligencia, educacion, poder)
        self.revolver = revolver
        self.porra = porra
        
########METODOS DE POLICIA VAN AQUI#############
    
    def atributos(self):
        super().atributos()
        print(".Revolver", self.revolver)
        print(".porra", self.porra)
        
        
#### USO DEL CONSTRUCTOR ####
# Almacenar en una variable, subclase(Atributo, atributo....)
# nombre = subclase(atributo1, atributo2, atributo3....)

anna = personaje("Anna Williams", dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6))
sebastian = policia("Sebastian Martinez", dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), 12, 4)
john = investigador("John Williams", dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), dados(3,6), 10, 6)
