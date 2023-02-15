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
        print(".daño:", self.DAÑO)
        print(".Usos por turno", self.UXT)
        print(".Critico:", self.CRIT)
        print(".Resistencia:", self.RES)
        print(".Peso:", self.WEIGHT)
        print(".Precio:", self.PRICE)
        print(".Disponibilidad", self.DIS)




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
            for x in range(1, self.UXT + 1):
                if self.BALAS > 0:
                    self.BALAS -= 1
                    print("Bang!")
                else:
                    print("click!")
    
    def recargar(self,cantidad):
        if self.BALAS == 0 and cantidad == "full":
            self.BALAS = 6
            

cuchillo = armabasica("Cuchillo", "CC", 4, 2, 33, 10, 1, 5, "Si")
revolver = armaproyectil("Revolver", "Fuego", 12, 2, 10, 20, 3, 25, "Si", 20, 6, 6)


