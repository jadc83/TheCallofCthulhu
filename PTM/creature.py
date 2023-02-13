from dado import dados
class criatura:
    
    def __init__(self, nombre, fuerza, constitucion, tamaño, destreza, inteligencia,  poder):
        """Metodo constructor."""
        self.nombre = nombre
        self.FUE = fuerza
        self.CON = constitucion
        self.TAM = tamaño
        self.DES = destreza
        self.INT = inteligencia
        self.POD = poder
        self.HP = ( self.TAM + self.CON ) / 2
        self.MP = self.POD
        
########METODOS DE CRIATURA VAN AQUI#############

    def atributos(self):
        """Muestra los atributos"""
        print(".Nombre:", self.nombre)
        print(".FUE:", self.FUE)
        print(".CON:", self.CON)
        print(".TAM", self.TAM)
        print(".DES:", self.DES)
        print(".INT:", self.INT)
        print(".POD:", self.POD)
        print(".HP", self.HP)
        print(".MP", self.MP)

class primigenio(criatura):
    
    def __init__(self, nombre, fuerza, constitucion, tamaño, destreza, inteligencia, poder):
        super().__init__(nombre, fuerza, constitucion, tamaño, destreza, inteligencia, poder)
        
########METODOS DE PRIMIGENIO VAN AQUI#############
    
    def atributos(self):    
        super().atributos()
        
cthulhu = primigenio("Cthulhu", dados(24,6), dados(50,6), dados(50,6), dados(19,6), dados(55,6), dados(600,6))
