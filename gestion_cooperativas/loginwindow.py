import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from mainwindow import MainWindow
from list import List


class VentanaLogin(QMainWindow):
    def __init__(self, usuarios: List, app):
        super().__init__()
        self.usuarios = usuarios
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(100, 100, 300, 200)
        self.app = app

        self.initUI()

    def initUI(self):
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Diseño vertical para los widgets
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Etiqueta y cuadro de texto para el correo electrónico
        label_email = QLabel("Correo Electrónico:")
        layout.addWidget(label_email)
        self.input_email = QLineEdit()
        layout.addWidget(self.input_email)

        # Etiqueta y cuadro de texto para la contraseña
        label_password = QLabel("Contraseña:")
        layout.addWidget(label_password)
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_password)

        # Botón para mostrar u ocultar la contraseña
        self.btn_show_hide_password = QPushButton("")
        self.btn_show_hide_password.setCheckable(True)
        self.btn_show_hide_password.clicked.connect(self.toggle_show_hide_password)
        layout.addWidget(self.btn_show_hide_password)

        # Botón de inicio de sesión
        btn_login = QPushButton("Iniciar Sesión")
        btn_login.clicked.connect(self.login)
        layout.addWidget(btn_login)

    def toggle_show_hide_password(self):
        if self.btn_show_hide_password.isChecked():
            self.input_password.setEchoMode(QLineEdit.Normal)
            self.btn_show_hide_password.setText("Ocultar Contraseña")
        else:
            self.input_password.setEchoMode(QLineEdit.Password)
            self.btn_show_hide_password.setText("Mostrar Contraseña")

    def login(self):
        email = self.input_email.text()
        password = self.input_password.text()
        for usuario in self.usuarios:
            if email == usuario.email and password == usuario.password:
                self.close()
                window = MainWindow(self.app)
                window.show()
                while True:
                    self.app.processEvents()
            else:
                pass
        QMessageBox.warning(self, "Inicio de Sesión", "Usuario o contraseña incorrectos")


