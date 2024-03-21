import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QTableWidget, QLabel, QLineEdit, \
    QTableWidgetItem, QDialog, QInputDialog, QHBoxLayout, QMessageBox
from usuario import Usuario
from list import List
from adduserwindow import AddUserDialog
import random


class VentanaUsuarios(QMainWindow):
    def __init__(self, titulo, app, usuarios: List = Usuario):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setFixedSize(640, 480)
        self.app = app
        self.usuarios = usuarios

        # Crear layout principal
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)

        self.tableWidget.setHorizontalHeaderLabels(["Código", "Nombre", "Correo", "Puesto", "Estado"])

        self.add_user_button = QPushButton("Agregar Usuario")
        self.add_user_button.clicked.connect(self.open_add_user_dialog)

        self.modify_button = QPushButton("Modificar Valor Seleccionado")
        self.modify_button.clicked.connect(self.modify_selected_value)

        self.modify_password_button = QPushButton("Modificar contraseña")
        self.modify_password_button.clicked.connect(self.modify_password)

        self.delete_user_button = QPushButton("Eliminar usuario")
        self.delete_user_button.clicked.connect(self.delete_user)

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.add_user_button)
        horizontal_layout.addWidget(self.modify_button)
        horizontal_layout.addWidget(self.modify_password_button)
        horizontal_layout.addWidget(self.delete_user_button)

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addLayout(horizontal_layout)

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)
        self.inicializar()

    def open_add_user_dialog(self):
        dialog = AddUserDialog(self.usuarios)
        if dialog.exec_():
            usercode = random.randint(1000, 9999)
            name = dialog.nombre_edit.text()
            email = dialog.correo_edit.text()
            job = dialog.puesto_edit.text()
            status = dialog.estado_edit.text()
            password = dialog.password_edit.text()
            nuevo_usuario = Usuario(email, password, str(usercode), name, job, status)
            self.usuarios.prepend(nuevo_usuario)
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(usercode)))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(name))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(email))
            self.tableWidget.setItem(row_position, 3, QTableWidgetItem(job))
            self.tableWidget.setItem(row_position, 4, QTableWidgetItem(status))

    def inicializar(self):
        row_position = self.tableWidget.rowCount()
        for usuario in self.usuarios:
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(usuario.usercode))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(usuario.name))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(usuario.email))
            self.tableWidget.setItem(row_position, 3, QTableWidgetItem(usuario.job))
            self.tableWidget.setItem(row_position, 4, QTableWidgetItem(usuario.status))

    def modify_password(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            for item in selected_items:
                row = item.row()
                column = item.column()
                value = self.usuarios.remove_at(row)
                new_value, ok = QInputDialog.getText(self, "Modificar Contraseña",
                                                     f"Ingrese la nueva contraseña de {value.name}:")
                if ok:
                    if row == 0:
                        objeto = value
                    elif row == len(self.usuarios) - 1:
                        objeto = value
                    else:
                        objeto = value
                    password = new_value
                    objeto_modificado = Usuario(objeto.email, password, objeto.usercode, objeto.name, objeto.job, objeto.status)
                    self.usuarios.prepend(objeto_modificado)

    def modify_selected_value(self):
        selected_items = self.tableWidget.selectedItems()

        if selected_items:
            for item in selected_items:
                row = item.row()
                column = item.column()
                new_value, ok = QInputDialog.getText(self, "Modificar Valor",
                                                     f"Ingrese el nuevo valor para ({row}, {column}):")
                if ok:
                    if row == 0:
                        objeto = self.usuarios.pop()
                    elif row == len(self.usuarios) - 1:
                        objeto = self.usuarios.shift()
                    else:
                        objeto = self.usuarios.remove_at(row)
                    name = objeto.name
                    email = objeto.email
                    job = objeto.job
                    status = objeto.status
                    if column == 1:
                        name = new_value
                    elif column == 2:
                        email = new_value
                    elif column == 3:
                        job = new_value
                    elif column == 4:
                        status = new_value
                    objeto_modificado = Usuario(email, objeto.password, objeto.usercode, name, job, status)
                    self.usuarios.prepend(objeto_modificado)
                    self.tableWidget.setItem(row, column, QTableWidgetItem(new_value))

    def delete_user(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            for item in selected_items:
                row = item.row()
                column = item.column()
                value = self.usuarios.remove_at(row)
                QMessageBox.information(self, 'Usuario eliminado', f'Se ha eliminado el usuario {value.name}.')
                self.tableWidget.removeRow(row)
