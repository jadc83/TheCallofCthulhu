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
        self.ESTADO = estado
        self.INVENTARIO = []
        self.DEF = self.CON
        self.ATK = round(( self.FUE + self.CON ) / 2, 0)
        self.DAMAGE = 0
        self.SHIELD = 0
        self.ARMA = "Nada"

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
        print("Inventario\n", [x for x in self.INVENTARIO])
        
    def status(self):
        "Muestra un breve resumen del personaje."
        if self.HP >= 1:
            print("Esta vivo.")
            print(f"HP: {self.HP} ")
            if self.ARMA == "Nada":
                print(f"Equipado con: {self.ARMA} --> DmgOutput: {self.ATK}")
            else:
                print(f"Equipado con: {self.ARMA} --> DmgOutput: {self.DAMAGE}") 
            return [ x.nombre for x in self.INVENTARIO ] 
        else:
            print("Esta muerto")
    
    def morir(self):
        "Para admin, Mata al personaje sobre el que se use."
        self.ESTADO = "Muerto"
        self.HP = 0
        return self.nombre, "ha muerto."
    
    def resucitar(self):
        "Para admin, Resucita al personaje sobre el que se use."
        self.ESTADO = "Vivo"
        self.HP = 100
        return self.nombre, "ha resucitado."
    
    def equipar(self, objeto):
        if objeto in self.INVENTARIO:
            if objeto.CLASE == "Ofensiva":
                self.DAMAGE += objeto.DAÑO
                self.ARMA = objeto.nombre
                return f"{objeto.nombre} se ha equipado"
    
    def desequipar(self, objeto):
            self.DAMAGE = 0
            self.ARMA = "Nada"
            return f"{objeto.nombre} se ha guardado."
    
    ########################################################################### METODOS DE INVENTARIO ####################################################################
    
    def coger(self, objeto):
        self.INVENTARIO.append(objeto)
        
    def soltar(self, objeto):
        if objeto in self.INVENTARIO:
            self.INVENTARIO.pop(self.INVENTARIO.index(objeto))
            return f"Se ha soltado {objeto.nombre}"
    
    def mirar_en_mochila(self):
        if self.INVENTARIO == []:
            return "Mochila vacia."
        else:
            return [ x.nombre for x in self.INVENTARIO ]
    
    def saquear(self, objetivo):
        if objetivo.HP == 0:
            if objetivo.INVENTARIO != []:
                print(f"Has saqueado { [ x.nombre for x in objetivo.INVENTARIO ]}")
                self.INVENTARIO.append(objetivo.INVENTARIO)
                objetivo.INVENTARIO.clear()
            else:
                return "Inventario vacio."
    
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
