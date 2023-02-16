class mueble:
    
    def __init__(self, nombre, descripcion, resistencia, inventario):
        """Metodo constructor."""
        self.nombre = nombre
        self.INFO = descripcion
        self.RES = resistencia
        self.INV = inventario


    def atributos(self):
        """Muestra los atributos"""
        print(".Nombre:", self.nombre)
        print(".Descripcion:", self.INFO)
        print(".RES:", self.RES)
        print("Cajones:", self.INV)
