from dado import dados
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
        self.__ESTADO = estado
        self.INVENTARIO = []

    def atributos(self):
        """Muestra los atributos"""
        print(".Nombre:", self.nombre)
        print(".FUE:", self.FUE)
        print(".CON:", self.CON)
        print(".DES:", self.DES)
        print(".INT:", self.INT)
        print(".HP", self.HP)
        print(".MP", self.MP)
        print(".Estado:", self.__ESTADO)
        print("Inventario\n", [x for x in self.INVENTARIO])
        
    def esta_vivo(self):
        if self.HP > 0:
            print("Esta vivo.")
        elif self.HP <= 0:
            self.__ESTADO = "Muerto"
    
    def morir(self):
        self.__ESTADO = "Muerto"
        print(self.nombre, "ha muerto.")
    
    def resucitar(self):
        self.__ESTADO = "Vivo"
        print(self.nombre, "ha resucitado.")
        
    def recoger(self,objeto):
        self.INVENTARIO.append(objeto)
        print("Se ha recogido", objeto.nombre)
    
    def soltar(self,objeto):
        self.INVENTARIO.pop(self.INVENTARIO.index(objeto))
        print("Se ha soltado", objeto.nombre)
    
    def mochila(self):
        for x in self.INVENTARIO:
            print(x.nombre)

############################################################################## METODOS DE COMBATE #######################################################################

    def puñetazo(self, enemigo):
        enemigo.HP -= dados(2,4)
        print(self.nombre, "lanza un puñetazo!")
        if enemigo.HP < 1:
            enemigo.morir()
        else:
            print("A", enemigo.nombre,"le quedan", enemigo.HP,"puntos de vida.")
    
    def patada(self, enemigo):
        enemigo.HP -= dados(2,6)
        print(self.nombre, "lanza una patada!!")
        if enemigo.HP < 1:
            enemigo.morir()
        else:
            print("A", enemigo.nombre,"le quedan", enemigo.HP,"puntos de vida.")
            
############################################################################ HABILIDADES ###############################################################################

        
