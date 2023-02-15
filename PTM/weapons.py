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
    
    def __init__(self, nombre, tipo, daño, uxt, critico, resistencia, peso, precio, disponible, alcance, cargador, balas):
        super().__init__(nombre, tipo, daño, uxt, critico, resistencia, peso, precio, disponible)
        self.ALCANCE = alcance
        self.CARGADOR = cargador
        self.BALAS = balas


    def atributos(self):
        super().atributos()
        print(".Alcance", self.ALCANCE)
        print(".Cargador:", self.CARGADOR)
        print(".Balas", self.BALAS)
        
        
    def disparar(self):
        if self.BALAS == 0:
            print("Oops...")
        else:
            for x in range(1, self.UXT + 1):
                print("Bang!")
                self.BALAS = self.BALAS - 1
               
                
    def recargar(self):
        while self.BALAS != self.CARGADOR:
            self.BALAS = self.BALAS + 1
            print("Plink.")
    
    
    def descargar(self):
        while self.BALAS > 0:
            self.BALAS = self.BALAS - 1
            print("Plonk.")
            

cuchillo = armabasica("Cuchillo", "CC", 4, 2, 33, 10, 1, 5, "Si")
revolver = armaproyectil("Revolver", "Fuego", 12, 2, 10, 20, 3, 25, "Si", 20, 6, 6)


