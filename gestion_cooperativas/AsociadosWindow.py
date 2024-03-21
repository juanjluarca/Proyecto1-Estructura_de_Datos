import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QMessageBox, QFileDialog
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QDialog, QListWidget, QDialogButtonBox
from PyQt5.QtWidgets import QApplication
import random
from list import List


class Asociado:
    def __init__(self, nombre, direccion, telefonos, dpi, nit, archivos_adjuntos=None, referencias_personales=None):
        self.codigo_asociado = random.randint(1000, 9999)
        self.nombre = nombre
        self.direccion = direccion
        self.telefonos = telefonos
        self.dpi = dpi
        self.nit = nit
        self.archivos_adjuntos = archivos_adjuntos or []
        self.referencias_personales = referencias_personales or []

    def actualizar_datos(self, nombre=None, direccion=None, telefonos=None, dpi=None, nit=None):
        if nombre:
            self.nombre = nombre
        if direccion:
            self.direccion = direccion
        if telefonos:
            self.telefonos = telefonos
        if dpi:
            self.dpi = dpi
        if nit:
            self.nit = nit

    def agregar_archivo_adjunto(self, archivo):
        if os.path.isfile(archivo):  # Verificar si el archivo existe
            with open(archivo, 'rb') as file:
                contenido = file.read()
            self.archivos_adjuntos.append(contenido)
        else:
            print(f"El archivo '{archivo}' no existe.")

    def eliminar_archivos_adjuntos(self):
        self.archivos_adjuntos.clear()

    def agregar_referencia_personal(self, referencia):
        self.referencias_personales.append(referencia)

    def eliminar_referencia_personal(self, referencia):
        if referencia in self.referencias_personales:
            self.referencias_personales.remove(referencia)

    def eliminar_cuenta(self, lista_asociados):
        for asociado in lista_asociados:
            if asociado.codigo_asociado == self.codigo_asociado:
                lista_asociados.remove(asociado)
                return True
        return False


class VentanaRegistroAsociado(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Registro de Nuevo Asociado")
        self.setGeometry(100, 100, 400, 300)
        self.app = app
        self.asociados = List()  # Lista de asociados

        self.initUI()

    def initUI(self):
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Diseño vertical para los widgets
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Formulario para registro de nuevo asociado
        label_nombre = QLabel("Nombre:")
        self.input_nombre = QLineEdit()
        layout.addWidget(label_nombre)
        layout.addWidget(self.input_nombre)

        label_direccion = QLabel("Dirección:")
        self.input_direccion = QLineEdit()
        layout.addWidget(label_direccion)
        layout.addWidget(self.input_direccion)

        label_telefonos = QLabel("Teléfonos:")
        self.input_telefonos = QLineEdit()
        layout.addWidget(label_telefonos)
        layout.addWidget(self.input_telefonos)

        label_dpi = QLabel("Número de DPI:")
        self.input_dpi = QLineEdit()
        layout.addWidget(label_dpi)
        layout.addWidget(self.input_dpi)

        label_nit = QLabel("Número de NIT:")
        self.input_nit = QLineEdit()
        layout.addWidget(label_nit)
        layout.addWidget(self.input_nit)

        # Botón de registro
        btn_registrar = QPushButton("Registrar Asociado")
        btn_registrar.clicked.connect(self.registrar_asociado)
        layout.addWidget(btn_registrar)

        self.lista_asociados = QListWidget()
        layout.addWidget(self.lista_asociados)

        btn_mostrar_asociados = QPushButton("Mostrar Todos los Asociados")
        btn_mostrar_asociados.clicked.connect(self.mostrar_todos_asociados)
        layout.addWidget(btn_mostrar_asociados)

        # Botón de eliminación
        btn_eliminar = QPushButton("Eliminar Cuenta")
        btn_eliminar.clicked.connect(self.abrir_ventana_eliminar_cuenta)
        layout.addWidget(btn_eliminar)

        # Botón para cargar archivos adjuntos
        btn_cargar_archivo = QPushButton("Cargar Archivo Adjunto")
        btn_cargar_archivo.clicked.connect(self.cargar_archivo_adjunto)
        layout.addWidget(btn_cargar_archivo)

        btn_actualizar_datos = QPushButton("Actualizar Datos del Asociado")
        btn_actualizar_datos.clicked.connect(self.actualizar_datos_asociado)
        layout.addWidget(btn_actualizar_datos)

        btn_agregar_recomendacion = QPushButton("Agregar Recomendación")
        btn_agregar_recomendacion.clicked.connect(self.agregar_recomendacion)
        layout.addWidget(btn_agregar_recomendacion)

        self.lista_archivos_adjuntos = QListWidget()
        layout.addWidget(self.lista_archivos_adjuntos)



    def registrar_asociado(self):
        nombre = self.input_nombre.text()
        direccion = self.input_direccion.text()
        telefonos = self.input_telefonos.text()
        dpi = self.input_dpi.text()
        nit = self.input_nit.text()

        nuevo_asociado = Asociado(nombre, direccion, telefonos, dpi, nit)
        self.asociados.append(nuevo_asociado)

        self.lista_asociados.addItem(f"{nombre} - {nuevo_asociado.codigo_asociado}")
        QMessageBox.information(self, "Registro Exitoso", "El asociado ha sido registrado exitosamente.")

        self.input_nombre.clear()
        self.input_direccion.clear()
        self.input_telefonos.clear()
        self.input_dpi.clear()
        self.input_nit.clear()

    def abrir_ventana_eliminar_cuenta(self):
        # Ventana para eliminar cuenta
        self.ventana_eliminar = QDialog(self)
        self.ventana_eliminar.setWindowTitle("Eliminar Cuenta de Asociado")
        self.ventana_eliminar.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()
        self.ventana_eliminar.setLayout(layout)

        label_codigo = QLabel("Código de Asociado:")
        input_codigo = QLineEdit()
        layout.addWidget(label_codigo)
        layout.addWidget(input_codigo)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(lambda: self.eliminar_cuenta(int(input_codigo.text())))
        buttons.rejected.connect(self.ventana_eliminar.reject)
        layout.addWidget(buttons)

        self.ventana_eliminar.show()

    def eliminar_cuenta(self, codigo):
        asociado_a_eliminar = None
        for asociado in self.asociados:
            if asociado.codigo_asociado == codigo:
                asociado_a_eliminar = asociado
                break

        if asociado_a_eliminar:
            confirmacion = QMessageBox.question(self, "Confirmar Eliminación",
                                                f"¿Está seguro de eliminar la cuenta del asociado {asociado_a_eliminar.nombre}? Esta acción no se puede deshacer.",
                                                QMessageBox.Yes | QMessageBox.No)
            if confirmacion == QMessageBox.Yes:
                if self.asociados.remove_asociado(asociado_a_eliminar):
                    asociado_a_eliminar.eliminar_archivos_adjuntos()
                    QMessageBox.information(self, "Eliminación Exitosa", "La cuenta ha sido eliminada correctamente.")
                    # Actualizar la lista visual de asociados
                    self.actualizar_lista_asociados()
                    self.lista_archivos_adjuntos.clear()
                else:
                    QMessageBox.warning(self, "Error", "No se pudo encontrar el asociado con el código especificado.")
        else:
            QMessageBox.warning(self, "Error", "No se encontró ningún asociado con el código especificado.")

    def actualizar_lista_asociados(self):
        # Limpiar la lista visual de asociados
        self.lista_asociados.clear()
        # Volver a agregar los asociados restantes a la lista visual
        for asociado in self.asociados:
            self.lista_asociados.addItem(f"{asociado.nombre} - {asociado.codigo_asociado}")

    def actualizar_datos_asociado(self):
        try:
            if self.lista_asociados.currentRow() >= 0:
                asociado_index = self.lista_asociados.currentRow()
                asociado_actual = self.asociados[asociado_index]

                # Obtener los nuevos datos desde los campos de entrada
                nuevo_nombre = self.input_nombre.text()
                nueva_direccion = self.input_direccion.text()
                nuevos_telefonos = self.input_telefonos.text()
                nuevo_dpi = self.input_dpi.text()
                nuevo_nit = self.input_nit.text()

                # Actualizar los datos del asociado
                asociado_actual.actualizar_datos(nombre=nuevo_nombre, direccion=nueva_direccion,
                                                 telefonos=nuevos_telefonos,
                                                 dpi=nuevo_dpi, nit=nuevo_nit)

                # Actualizar la lista visual de asociados
                self.actualizar_lista_asociados()

                QMessageBox.information(self, "Actualización Exitosa",
                                        "Los datos del asociado han sido actualizados correctamente.")
            else:
                QMessageBox.warning(self, "Error", "Seleccione un asociado antes de actualizar los datos.")
        except Exception as e:
            QMessageBox.critical(self, "Error",
                                 f"Se ha producido un error al actualizar los datos del asociado: {str(e)}")

    def actualizar_lista_archivos_adjuntos(self, asociado):
        # Limpiar la lista visual de archivos adjuntos
        self.lista_archivos_adjuntos.clear()
        # Volver a agregar los archivos adjuntos del asociado a la lista visual
        for archivo in asociado.archivos_adjuntos:
            self.lista_archivos_adjuntos.addItem(f"Nombre del archivo: {archivo}")


    def cargar_archivo_adjunto(self):
        file_dialog = QFileDialog(self)
        file_dialog.setModal(False)  # Establecer el diálogo como no modal
        file_dialog.setNameFilter("Archivos PDF (*.pdf)")  # Filtrar archivos PDF
        file_dialog.setViewMode(QFileDialog.Detail)

        if file_dialog.exec_():
            if self.lista_asociados.currentRow() >= 0:
                asociado_index = self.lista_asociados.currentRow()
                asociado_actual = self.asociados[asociado_index]

                file_paths = file_dialog.selectedFiles()
                pdf_path = file_paths[0]

                try:
                    if os.path.exists(pdf_path):
                        with open(pdf_path, 'rb') as file:
                            contenido = file.read()
                        asociado_actual.archivos_adjuntos.append(contenido)
                        QMessageBox.information(self, "Carga Exitosa",
                                                "El archivo adjunto ha sido cargado exitosamente.")
                        self.actualizar_lista_archivos_adjuntos(asociado_actual)  # Aquí se llama al método para actualizar la lista de archivos adjuntos
                    else:
                        QMessageBox.warning(self, "Error", "El archivo seleccionado no existe.")
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Error al cargar el archivo adjunto: {str(e)}")
            else:
                QMessageBox.warning(self, "Error", "Seleccione un asociado antes de cargar archivos adjuntos.")

    def agregar_recomendacion(self):
        file_dialog = QFileDialog(self)
        file_dialog.setModal(False)  # Establecer el diálogo como no modal
        file_dialog.setNameFilter("Archivos PDF (*.pdf)")  # Filtrar archivos PDF
        file_dialog.setViewMode(QFileDialog.Detail)

        if file_dialog.exec_():
            if self.lista_asociados.currentRow() >= 0:
                asociado_index = self.lista_asociados.currentRow()
                asociado_actual = self.asociados[asociado_index]

                file_paths = file_dialog.selectedFiles()
                pdf_path = file_paths[0]

                try:
                    if os.path.exists(pdf_path):
                        with open(pdf_path, 'rb') as file:
                            contenido = file.read()
                        asociado_actual.archivos_adjuntos.append(contenido)
                        QMessageBox.information(self, "Carga Exitosa",
                                                "La Recomendacion ha sido cargado exitosamente.")
                        self.actualizar_lista_archivos_adjuntos(
                            asociado_actual)
                    else:
                        QMessageBox.warning(self, "Error", "La recomendacion seleccionada no existe.")
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Error al cargar la Recomendacion: {str(e)}")
            else:
                QMessageBox.warning(self, "Error", "Seleccione un asociado antes de cargar la recomendacion.")

    def mostrar_todos_asociados(self):
        if len(self.asociados) == 0:
            QMessageBox.information(self, "No hay asociados", "No hay asociados registrados.")
            return

        mensaje = "Todos los asociados registrados:\n\n"
        for asociado in self.asociados:
            mensaje += f"Código: {asociado.codigo_asociado}\n"
            mensaje += f"Nombre: {asociado.nombre}\n"
            mensaje += f"Dirección: {asociado.direccion}\n"
            mensaje += f"Teléfonos: {asociado.telefonos}\n"
            mensaje += f"DPI: {asociado.dpi}\n"
            mensaje += f"NIT: {asociado.nit}\n"
            if asociado.archivos_adjuntos:
                mensaje += "Archivos Adjuntos:\n"
                for adjunto in asociado.archivos_adjuntos:
                    mensaje += f" - {adjunto}\n"
            else:
                mensaje += "Sin archivos adjuntos.\n"
            if asociado.referencias_personales:
                mensaje += "Recomendaciones:\n"
                for recomendacion in asociado.referencias_personales:
                    mensaje += f" - {recomendacion}\n"
            else:
                mensaje += "Sin recomendaciones.\n"
            mensaje += "\n"

        QMessageBox.information(self, "Todos los asociados", mensaje)