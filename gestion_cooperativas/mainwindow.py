from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from userswindow import VentanaUsuarios
from bankloanwindow import VentanaPrestamos
from AsociadosWindow import VentanaRegistroAsociado

class MainWindow(QMainWindow):
    def __init__(self, app, usuarios):
        super().__init__()
        self.ventana_1 = None
        self.ventana_3 = None
        self.app = app
        self.ventana_2 = None
        self.usuarios = usuarios

        self.setWindowTitle("Ventana principal")
        self.setFixedSize(640, 480)

        # Creamos un widget central para la ventana principal
        widget_central = QWidget()

        # Creamos un layout vertical para el widget central
        layout_vertical = QVBoxLayout()
        # Creamos 3 botones y establecemos su tamaño fijo.
        boton_1 = QPushButton("Gestión de asociados")
        boton_1.setFixedSize(200, 60)
        boton_2 = QPushButton("Préstamos bancarios")
        boton_2.setFixedSize(200, 60)
        boton_3 = QPushButton("Usuarios")
        boton_3.setFixedSize(200, 60)

        # Creamos un layout horizontal auxiliar para centrar los botones.
        layout_horizontal1 = QHBoxLayout()
        layout_horizontal2 = QHBoxLayout()
        layout_horizontal3 = QHBoxLayout()

        # **Añadimos los botones al layout horizontal.**
        layout_horizontal1.addWidget(boton_1)
        layout_horizontal2.addWidget(boton_2)
        layout_horizontal3.addWidget(boton_3)

        # **Centramos los botones horizontalmente.**
        layout_horizontal1.setAlignment(Qt.AlignHCenter)
        layout_horizontal2.setAlignment(Qt.AlignHCenter)
        layout_horizontal3.setAlignment(Qt.AlignHCenter)

        # Añadimos el layout horizontal al layout vertical.
        layout_vertical.addLayout(layout_horizontal1)
        layout_vertical.addLayout(layout_horizontal2)
        layout_vertical.addLayout(layout_horizontal3)

        # Establecemos el layout vertical como el layout del widget central
        widget_central.setLayout(layout_vertical)
        # Establecemos el widget central como el widget principal de la ventana
        self.setCentralWidget(widget_central)

        # Conectamos los botones a las funciones para abrir las otras ventanas
        boton_1.clicked.connect(self.abrir_ventana_1)
        boton_2.clicked.connect(self.abrir_ventana_2)
        boton_3.clicked.connect(self.abrir_ventana_3)

    def abrir_ventana_1(self):
        self.ventana_1 = VentanaRegistroAsociado(self.app)
        self.ventana_1.show()
        # Bucle para mantener la ventana abierta hasta que se cierre manualmente.
        while True:
            self.app.processEvents()


    def abrir_ventana_2(self):
        self.ventana_2 = VentanaPrestamos("Préstamos", self.app, self.usuarios)
        self.ventana_2.show()
        # Bucle para mantener la ventana abierta hasta que se cierre manualmente.
        while True:
            self.app.processEvents()


    def abrir_ventana_3(self):
        self.ventana_3 = VentanaUsuarios("Usuarios", self.app)
        self.ventana_3.show()
        # Bucle para mantener la ventana abierta hasta que se cierre manualmente.
        while True:
            self.app.processEvents()
