from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
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
        self.archivos_adjuntos.append(archivo)

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
    def __init__(self, app, asociados):
        super().__init__()
        self.asociados = asociados
        self.setWindowTitle("Registro de Nuevo Asociado")
        self.setGeometry(100, 100, 400, 300)
        self.app = app

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

    def registrar_asociado(self):
        nombre = self.input_nombre.text()
        direccion = self.input_direccion.text()
        telefonos = self.input_telefonos.text()
        dpi = self.input_dpi.text()
        nit = self.input_nit.text()

        nuevo_asociado = Asociado(nombre, direccion, telefonos, dpi, nit)
        self.asociados.append(nuevo_asociado)

        QMessageBox.information(self, "Registro Exitoso", "El asociado ha sido registrado exitosamente.")

        self.input_nombre.clear()
        self.input_direccion.clear()
        self.input_telefonos.clear()
        self.input_dpi.clear()
        self.input_nit.clear()

    def abrir_ventana_eliminar_cuenta(self):
        # Ventana para eliminar cuenta
        ventana_eliminar = QDialog(self)
        ventana_eliminar.setWindowTitle("Eliminar Cuenta de Asociado")
        ventana_eliminar.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()
        ventana_eliminar.setLayout(layout)

        label_codigo = QLabel("Código de Asociado:")
        input_codigo = QLineEdit()
        layout.addWidget(label_codigo)
        layout.addWidget(input_codigo)

        btn_eliminar = QPushButton("Eliminar Cuenta")
        btn_eliminar.clicked.connect(lambda: self.eliminar_cuenta(int(input_codigo.text())))
        layout.addWidget(btn_eliminar)

        ventana_eliminar.exec_()

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
                if asociado_a_eliminar.eliminar_cuenta(self.asociados):
                    QMessageBox.information(self, "Eliminación Exitosa", "La cuenta ha sido eliminada correctamente.")
                else:
                    QMessageBox.warning(self, "Error", "No se pudo encontrar el asociado con el código especificado.")
        else:
            QMessageBox.warning(self, "Error", "No se encontró ningún asociado con el código especificado.")


