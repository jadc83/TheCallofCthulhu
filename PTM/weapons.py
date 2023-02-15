import sys
class armabasica:
    
    def __init__(self, nombre, tipo, daño, uxt, critico, resistencia, peso, precio, disponible):
        """Metodo constructor."""
        self.nombre = nombre
        self.TIPO = tipo
        self.DAÑO = daño
        self.UXT = uxt
        self.CRIT = critico
        self.RES = resistencia
        self.WEIGHT = peso
        self.PRICE = precio
        self.DIS = disponible

    def atributos(self):
        """Muestra los atributos"""
        print(".Nombre:", self.nombre)
        print(".Tipo:", self.TIPO)

class armaproyectil(armabasica):
    
    def __init__(self, nombre, tipo, daño, uxt, critico, resistencia, peso, precio, disponible, alcance, cargador, balas, seguro):
        super().__init__(nombre, tipo, daño, uxt, critico, resistencia, peso, precio, disponible)
        self.ALCANCE = alcance
        self.CARGADOR = cargador
        self.BALAS = balas
        self.SEGURO = seguro

    def atributos(self):
        super().atributos()
        print(".Alcance", self.ALCANCE)
        print(".Cargador:", self.CARGADOR)
        print(".Balas", self.BALAS)
        
    def seguro(self):
        self.SEGURO = not self.SEGURO
        if self.SEGURO:
            print("Seguro puesto")
        elif self.SEGURO == False:
            print("Sin seguro.")
            
    def disparar(self):
        if self.SEGURO:
            print("No dispara")
        else:
            if self.BALAS == 0:
                print("Oops...")
            else:
                for x in range(self.UXT):
                    print("Bang!")
                    self.BALAS -= 1
               
    def recargar(self):
        while self.BALAS != self.CARGADOR:
            self.BALAS += 1
            print("Plik.")
    
    def descargar(self):
        while self.BALAS > 0:
            self.BALAS -= 1
            print("Plok.")
            
###################### nombre ## tipo ## daño ## uxt ## critico ## resistencia ## peso ## precio ## disponible ## alcance ## cargador ## balas
cuchillo = armabasica("Cuchillo", "CC", 4, 2, 33, 10, 1, 5, "Si")
revolver = armaproyectil("Revolver", "Fuego", 12,  2, 10, 20,  3,  25, "Si", 20,  6,  6, True)
thompson = armaproyectil("Thompson", "Fuego", 15, 10,  5, 90, 20, 150, "Si", 45, 50, 50, True)


