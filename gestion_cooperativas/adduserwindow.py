from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from list import List


class AddUserDialog(QDialog):
    def __init__(self, usuarios: List):
        super().__init__()
        self.usuarios = usuarios

        self.setWindowTitle("Agregar Usuario")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()
        self.password_label = QLabel("Contraseña:")
        self.password_edit = QLineEdit()

        self.nombre_label = QLabel("Nombre:")
        self.nombre_edit = QLineEdit()

        self.correo_label = QLabel("Correo:")
        self.correo_edit = QLineEdit()

        self.puesto_label = QLabel("Puesto:")
        self.puesto_edit = QLineEdit()

        self.estado_label = QLabel("Estado:")
        self.estado_edit = QLineEdit()

        self.add_button = QPushButton("Agregar")
        self.add_button.clicked.connect(self.accept)

        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_edit)
        layout.addWidget(self.correo_label)
        layout.addWidget(self.correo_edit)
        layout.addWidget(self.puesto_label)
        layout.addWidget(self.puesto_edit)
        layout.addWidget(self.estado_label)
        layout.addWidget(self.estado_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.add_button)

        self.setLayout(layout)
