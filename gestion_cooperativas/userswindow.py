import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton


class VentanaUsuarios(QMainWindow):
    def __init__(self, titulo, app):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setFixedSize(640, 480)
        self.app = app

        # Crear layout principal
        layout_principal = QVBoxLayout()

        # Crear botón para cerrar
        boton_cerrar = QPushButton("Cerrar")

        # Agregar botón al layout
        layout_principal.addWidget(boton_cerrar)

        # Establecer el layout principal
        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

        # Conectar evento al botón
        boton_cerrar.clicked.connect(self.close)

        # Cerrar la ventana principal al cerrar la secundaria
        self.destroyed.connect(lambda: self.app.quit())
