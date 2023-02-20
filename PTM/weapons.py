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
        self.CLASE = "Ofensiva"

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
                    print(f'{self.nombre} ha disparado a {objetivo.nombre}')
                    print(f"A {objetivo.nombre} le quedan {objetivo.HP} puntos de vida")
                    if objetivo.HP < 1:
                        return objetivo.nombre, "ha muerto."
                        objetivo.morir()
                        break
                    
    def seguro(self, arma):
        if arma in self.INVENTARIO:
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
    
    def pinchar(self, arma, objetivo):
        if arma in self.INVENTARIO:
            objetivo.HP -= arma.DAÑO
            
        print(f'{self.nombre} ha pinshao a {objetivo.nombre}')
        print(f"A {objetivo.nombre} le quedan {objetivo.HP} puntos de vida")