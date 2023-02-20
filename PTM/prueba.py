import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        # Agregar un botón a la ventana
        self.boton = QPushButton('Haz clic aquí', self)
        self.boton.setGeometry(50, 50, 100, 50)

        # Conectarse al evento clic del botón
        self.boton.clicked.connect(self.on_boton_clic)

    def on_boton_clic(self):
        print('Se hizo clic en el botón')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())