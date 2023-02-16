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
        self.__INVENTARIO = []

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
        print("Inventario\n", [x for x in self.__INVENTARIO])
        
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
        
    def recoger(self, objeto):
        self.__INVENTARIO += objeto
        print("Se ha recogido", objeto.nombre)
    
    def soltar(self, objeto):
        self.__INVENTARIO.pop(self.__INVENTARIO.index(objeto))
        print("Se ha soltado", objeto.nombre)
    
    def mochila(self):
        for x in self.__INVENTARIO:
            print(x.nombre)
            
    def saquear(self, objetivo):
        if objetivo.__ESTADO == "Muerto":
            self.__INVENTARIO += objetivo.__INVENTARIO
            print(self.nombre, "ha saqueado:")
            objetivo.mochila()
            objetivo.__INVENTARIO.clear()
    
    def inspeccionar(self, objetivo):
        print(objetivo.INFO)
        
    def registrar(self, objetivo):
        self.__INVENTARIO += objetivo.INV
        self.mochila()


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
                
############################################################################ METODOS CON ARMAS ###############################################################################

    def disparar(self, arma, objetivo):
        if arma.SEGURO:
            print("No dispara")
        else:
            if arma.BALAS == 0:
                print("Oops...")
            else:
                for x in range(arma.USOS):
                    print("Bang!")
                    arma.BALAS -= 1
                    objetivo.HP -= arma.DAÑO
                    if objetivo.HP < 1:
                        objetivo.morir()
                        break
                    
    def seguro(self, arma):
        if arma in self.__INVENTARIO:
            arma.SEGURO = not arma.SEGURO
            if arma.SEGURO:
                print("Seguro puesto")
            elif arma.SEGURO == False:
                print("Sin seguro.")
        else:
            print("No dispones de tal arma.")
                           
    def recargar(self, arma):
        while arma.BALAS != arma.CARGADOR:
            arma.BALAS += 1
            print("Plik.")
    
    def descargar(self, arma):
        while arma.BALAS > 0:
            arma.BALAS -= 1
            print("Plok.")