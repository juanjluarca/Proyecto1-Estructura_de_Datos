
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from list import List
from loan import Loan

class VentanaPrestamos(QMainWindow):
    def __init__(self, titulo, app, usuarios):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setFixedSize(640, 480)
        self.app = app
        self.loans = List()
        self.new_window = QMainWindow()
        self.usuarios = usuarios
        self.pay_record = List()


        # Crear layout principal
        layout_principal = QVBoxLayout()

        #admin
        # Crear botón para cerrar
        boton_cerrar = QPushButton("Cerrar")
        boton_cerrar.setFixedSize(550, 40)
        boton_loan = QPushButton("Generar prestamo")
        boton_loan.setFixedSize(550, 40)
        boton_plan = QPushButton("Planes de credito")
        boton_plan.setFixedSize(550, 40)
        boton_approve = QPushButton("Aprobar prestamo")
        boton_approve.setFixedSize(550, 40)
        boton_see = QPushButton("Visualizar los prestamos")
        boton_see.setFixedSize(550, 40)
        boton_buy = QPushButton("Realizar pagos")
        boton_buy.setFixedSize(550, 40)

        # Agregar botón al layout
        layout_principal.addWidget(boton_loan)
        layout_principal.addWidget(boton_plan)
        layout_principal.addWidget(boton_approve)
        layout_principal.addWidget(boton_see)
        layout_principal.addWidget(boton_buy)
        layout_principal.addWidget(boton_cerrar)
        layout_principal.setAlignment(Qt.AlignHCenter)

        # Establecer el layout principal
        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

        # Conectar evento al botón
        boton_cerrar.clicked.connect(self.close)
        boton_loan.clicked.connect(self.request_loan)
        boton_see.clicked.connect(self.show_loans)

        # Cerrar la ventana principal al cerrar la secundaria
        self.destroyed.connect(lambda: self.app.quit())

    def create_loan(self):
        user = self.user
        code_user = self.user_code
        month = self.month_income.text()
        money = self.money.text()
        number_pay = self.number_pay.text()
        reason = self.reason.text()
        warranty = self.warranty.text()
        self.loan = Loan(user, code_user, money, reason, month, warranty, number_pay, self.pay_record)
        print('hola mundo')


    def search_user(self):
        code = self.user_code.text()
        for user in self.usuarios:
            if str(code) == user.usercode:
                self.user_code = code
                self.user = user.name
                QMessageBox.information(self.new_window, 'Los datos se encontraron', 'El codigo es correcto')
                return 0
            else:
                pass

        QMessageBox.warning(self.new_window, 'Valor no encotrado', 'El codigo no se encuntra en el sistma')
    def add_loan(self):
        self.loans.append(self.loan)
        QMessageBox.information(self.new_window, 'Confirmacion', 'Se ha agregado el prestamo')
        self.new_window.close()

    def request_loan(self):
        new_window = self.new_window
        new_window.setWindowTitle('Solicitud de prestamo')
        new_window.setFixedSize(500, 400)
        new_window.show()
        show_layout = QVBoxLayout()
        confir = QPushButton('Confirmar solicitud')
        confir.setFixedSize(400, 50)
        ver = QPushButton('Verificar datos de usuario')
        ver.setFixedSize(400, 50)
        text1 = QLabel('Codigo de usuario:')
        text1.setAlignment(Qt.AlignVCenter)
        text2 = QLabel('Ingresos que tiene al mes:')
        text2.setAlignment(Qt.AlignVCenter)
        text3 = QLabel('De cuanto es el prestamo:')
        text3.setAlignment(Qt.AlignVCenter)
        text4 = QLabel('Cuanto va a pagar por mes:')
        text4.setAlignment(Qt.AlignVCenter)
        text5 = QLabel('En que va emplear el dinero:')
        text5.setAlignment(Qt.AlignVCenter)
        text6 = QLabel('Cuanto va a dejar de garantia:')
        text6.setAlignment(Qt.AlignVCenter)
        self.user_code = QLineEdit()
        self.user_code.setFixedSize(400, 20)
        self.month_income = QLineEdit()
        self.month_income.setFixedSize(400, 20)
        self.money = QLineEdit()
        self.money.setFixedSize(400, 20)
        self.number_pay = QLineEdit()
        self.number_pay.setFixedSize(400, 20)
        self.reason = QLineEdit()
        self.reason.setFixedSize(400, 20)
        self.warranty = QLineEdit()
        self.warranty.setFixedSize(400, 20)
        show_layout.addWidget(text1)
        show_layout.addWidget(self.user_code)
        show_layout.addWidget(text2)
        show_layout.addWidget(self.month_income)
        show_layout.addWidget(text3)
        show_layout.addWidget(self.money)
        show_layout.addWidget(text4)
        show_layout.addWidget(self.number_pay)
        show_layout.addWidget(text5)
        show_layout.addWidget(self.reason)
        show_layout.addWidget(text6)
        show_layout.addWidget(self.warranty)
        show_layout.addWidget(ver)
        show_layout.addWidget(confir)
        show_layout.setAlignment(Qt.AlignHCenter)
        widget_central = QWidget()
        widget_central.setLayout(show_layout)
        new_window.setCentralWidget(widget_central)
        confir.clicked.connect(self.create_loan)
        ver.clicked.connect(self.search_user)


        while True:
            self.app.processEvents()

    def show_loans(self):
        new_window = QMainWindow()
        new_window.setWindowTitle('Mostrar prestamos')
        new_window.setFixedSize(800, 900)
        new_window.show()
        show_layoutV = QVBoxLayout()
        for loan in self.loans:
            show = QLabel(loan)
            show.setAlignment(Qt.AlignHCenter)
            show_layoutV.addWidget(show)

        widget_central = QWidget()
        widget_central.setLayout(show_layoutV)
        new_window.setCentralWidget(widget_central)


        while True:
            self.app.processEvents()



