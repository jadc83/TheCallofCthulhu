import sys
class armabasica:
    
    def __init__(self, nombre, tipo, daño, usos, critico, resistencia, peso, precio, disponible):
        """Metodo constructor."""
        self.nombre = nombre
        self.TIPO = tipo
        self.DAÑO = daño
        self.USOS = usos
        self.CRIT = critico
        self.RES = resistencia
        self.WEIGHT = peso
        self.PRICE = precio
        self.DIS = disponible

    def atributos(self):
        """Muestra los atributos"""
        print(".Nombre:", self.nombre)
        print(".Tipo:", self.TIPO)
        print(".Usos por turno:", self.USOS)

class armaproyectil(armabasica):
    
    def __init__(self, nombre, tipo, daño, usos, critico, resistencia, peso, precio, disponible, alcance, cargador, balas, seguro):
        super().__init__(nombre, tipo, daño, usos, critico, resistencia, peso, precio, disponible)
        self.ALCANCE = alcance
        self.CARGADOR = cargador
        self.BALAS = balas
        self.SEGURO = seguro

    def atributos(self):
        super().atributos()
        print(".Alcance", self.ALCANCE)
        print(".Cargador:", self.CARGADOR)
        print(".Balas", self.BALAS)
            
###################### 1_nombre## 2_tipo## 3_daño ## 4_uxt ## 5_critico ## 6_resistencia ## 7_peso ## 8_precio ## 9_disponible ## 10_alcance ## 11_cargador ## 12_balas



