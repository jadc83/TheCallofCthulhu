class personaje:
    
    def __init__(self, nombre, fuerza, constitucion, destreza, inteligencia, estado):
        """Metodo constructor."""
        self.nombre = nombre
        self.FUE = fuerza
        self.CON = constitucion
        self.DES = destreza
        self.INT = inteligencia
        self.HP = 100
        self.MP = self.INT
        self.ESTADO = estado

    def atributos(self):
        """Muestra los atributos"""
        print(".Nombre:", self.nombre)
        print(".FUE:", self.FUE)
        print(".CON:", self.CON)
        print(".DES:", self.DES)
        print(".INT:", self.INT)
        print(".HP", self.HP)
        print(".MP", self.MP)
        print(".Estado:", self.ESTADO)
    
    def morir(self):
            self.ESTADO = "Muerto"
            print(self.nombre, "ha muerto.")
    
    def resucitar(self):
            self.ESTADO = "Vivo"
            print(self.nombre, "ha resucitado.")
#############METODOS DE PERSONAJE VAN AQUI#############

class investigador(personaje):
    
    def __init__(self, nombre, fuerza, constitucion, destreza, inteligencia, estado):
        super().__init__(nombre, fuerza, constitucion, destreza, inteligencia, estado)

        
    def atributos(self):
        super().atributos()
        
    def esta_vivo(self):
        if self.HP > 0:
            print("Esta vivo.")
        elif self.HP <= 0:
            self.ESTADO = "Muerto"