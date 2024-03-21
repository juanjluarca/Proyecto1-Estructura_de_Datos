import pickle

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QHBoxLayout, QTableWidget, QTableWidgetItem
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
        boton_load = QPushButton("Cargar prestamos")
        boton_load.setFixedSize(550, 40)
        boton_save = QPushButton("Guardar prestamos")
        boton_save.setFixedSize(550, 40)

        # Agregar botón al layout
        layout_principal.addWidget(boton_loan)
        layout_principal.addWidget(boton_plan)
        layout_principal.addWidget(boton_approve)
        layout_principal.addWidget(boton_see)
        layout_principal.addWidget(boton_buy)
        layout_principal.addWidget(boton_save)
        layout_principal.addWidget(boton_load)
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
        boton_plan.clicked.connect(self.add_loan)
        boton_approve.clicked.connect(self.approve_loan)
        boton_buy.clicked.connect(self.pay_loan)
        boton_save.clicked.connect(self.save_data)
        boton_load.clicked.connect(self.load_data)

        # Cerrar la ventana principal al cerrar la secundaria
        self.destroyed.connect(lambda: self.app.quit())

    def create_loan(self):
        user = self.user
        code_user = self.user_code
        month = self.month_income.text()
        money = self.money.text()
        pay_month = self.pay_month.text()
        reason = self.reason.text()
        warranty = self.warranty.text()
        self.loan = Loan(user, code_user, money, reason, month, warranty, pay_month, '0')
        QMessageBox.information(self.new_window, 'Confirmacion de solicitud', 'Se ha realizado la configuracion')
        self.new_window.close()

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
        money = int(self.money.text())
        if money >= 5000:
            QMessageBox.warning(self.new_window, 'Erro', 'El prestamo excede lo que aprueba la coperativa')
        else:
            self.loans.append(self.loan)
            QMessageBox.information(self.new_window, 'Confirmacion', 'Se ha agregado el prestamo')
            self.new_window.close()

    def pay_loan(self):
        new_window = self.new_window
        new_window.setWindowTitle('Aprobar prestamos')
        new_window.setFixedSize(700, 500)
        new_window.show()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Código", "Cantidad a pagar", "Estado"])
        layout_main = QHBoxLayout()
        layoutV1 = QVBoxLayout()
        layoutV2 = QVBoxLayout()
        layoutV1.addWidget(self.tableWidget)
        text1 = QLabel('Ingrese el Id del prestamo:')
        text1.setAlignment(Qt.AlignVCenter)
        text2 = QLabel('Ingresa la cantidad a pagar')
        text2.setAlignment(Qt.AlignVCenter)
        self.Id = QLineEdit()
        self.Id.setFixedSize(400, 30)
        self.pay_money = QLineEdit()
        self.pay_money.setFixedSize(400, 30)
        confirm = QPushButton('Confirmar')
        confirm.setFixedSize(400, 30)
        layoutV2.addWidget(text1)
        layoutV2.addWidget(self.Id)
        layoutV2.addWidget(text2)
        layoutV2.addWidget(self.pay_money)
        layoutV2.addWidget(confirm)
        layoutV2.setAlignment(Qt.AlignHCenter)
        layoutV2.setAlignment(Qt.AlignVCenter)
        layout_main.addLayout(layoutV1)
        layout_main.addLayout(layoutV2)
        widget_central = QWidget()
        widget_central.setLayout(layout_main)
        new_window.setCentralWidget(widget_central)
        confirm.clicked.connect(self.search_loan_pay)
        self.inicializar_pay()
        while True:
            self.app.processEvents()

    def search_loan(self):
        code = self.Id.text()
        for loan in self.loans:
            if str(code) == loan.code1:
                if loan.status1 == 'Aprovado' or loan.status1 == 'En curso' or loan.status1 == 'Finalizado':
                    QMessageBox.warning(self.new_window, 'Error', 'El prestamo ya fue aprobado')
                    self.new_window.close()

                else:
                    loan.status1 = 'Aprovado'
                    QMessageBox.information(self.new_window, 'Los datos se encontraron', 'El prestamo ha sido aprobado')
                    self.new_window.close()
                    return 0
            else:
                pass

    def search_loan_pay(self):
        code = self.Id.text()
        pay = self.pay_money.text()
        for loan in self.loans:
            if str(code) == loan.code1:
                if loan.status1 == 'Creado':
                    QMessageBox.warning(self.new_window, 'Error', 'El prestamo no ha sido aprobado')
                else:
                    self.pay_act = int(loan.pay_act1) - int(pay)
                    if self.pay_act <= 0:
                        loan.pay_act1 = str(self.pay_act)
                        loan.status1 = 'Finalizado'
                        self.pay_record2 = int(loan.pay_record1) + 1
                        loan.pay_record1 = str(self.pay_record2)

                    else:
                        loan.pay_act1 = str(self.pay_act)
                        loan.status1 = 'En curso'
                        self.pay_record2 = int(loan.pay_record1) + 1
                        loan.pay_record1 = str(self.pay_record2)

                    QMessageBox.information(self.new_window, 'Pago efectuado', 'El pago se ha efectuado de manera correcta')
                    self.new_window.close()
                    return 0

            else:
                pass

    def inicializar_show(self):
        row_position = self.tableWidget.rowCount()
        for loan in self.loans:
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(loan.code1))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(loan.user1))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(loan.user_code1))
            self.tableWidget.setItem(row_position, 3, QTableWidgetItem(loan.status1))
            self.tableWidget.setItem(row_position, 4, QTableWidgetItem(loan.money1))
            self.tableWidget.setItem(row_position, 5, QTableWidgetItem(loan.pay_act1))
            self.tableWidget.setItem(row_position, 6, QTableWidgetItem(loan.pay_record1))



    def inicializar_approve(self):
        row_position = self.tableWidget.rowCount()
        for loan in self.loans:
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(loan.code1))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(loan.pay_act1))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(loan.status1))

    def inicializar_pay(self):
        row_position = self.tableWidget.rowCount()
        for loan in self.loans:
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(loan.code1))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(loan.money1))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(loan.status1))

    def approve_loan(self):
        new_window = self.new_window
        new_window.setWindowTitle('Aprobar prestamos')
        new_window.setFixedSize(700, 500)
        new_window.show()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Código", "Nombre", "Estado"])
        layout_main = QHBoxLayout()
        layoutV1 = QVBoxLayout()
        layoutV2 = QVBoxLayout()
        layoutV1.addWidget(self.tableWidget)
        text1 = QLabel('Ingrese el Id del prestamo:')
        text1.setAlignment(Qt.AlignVCenter)
        self.Id = QLineEdit()
        self.Id.setFixedSize(400, 30)
        confirm = QPushButton('Confirmar')
        confirm.setFixedSize(400, 30)
        layoutV2.addWidget(text1)
        layoutV2.addWidget(self.Id)
        layoutV2.addWidget(confirm)
        layoutV2.setAlignment(Qt.AlignHCenter)
        layoutV2.setAlignment(Qt.AlignVCenter)
        layout_main.addLayout(layoutV1)
        layout_main.addLayout(layoutV2)
        widget_central = QWidget()
        widget_central.setLayout(layout_main)
        new_window.setCentralWidget(widget_central)
        confirm.clicked.connect(self.search_loan)
        self.inicializar_approve()

        while True:
            self.app.processEvents()


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
        self.pay_month = QLineEdit()
        self.pay_month.setFixedSize(400, 20)
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
        show_layout.addWidget(self.pay_month)
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
        new_window = self.new_window
        new_window.setWindowTitle('Mostrar prestamos')
        new_window.setFixedSize(800, 900)
        new_window.show()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["Código", "Nombre", "Codigo asociado", "Estado", "Cantidad a pagar", "Cantidad actual", "Pagos efectuados"])
        show_layoutV = QVBoxLayout()
        show_layoutV.setAlignment(Qt.AlignHCenter)
        show_layoutV.addWidget(self.tableWidget)
        self.inicializar_show()
        widget_central = QWidget()
        widget_central.setLayout(show_layoutV)
        new_window.setCentralWidget(widget_central)
        while True:
            self.app.processEvents()

    def load_data(self):
        try:
            with open('Save_loans.dat', 'rb') as file:
                self.loans = pickle.load(file)
                QMessageBox.information(self.new_window, 'Carga prestamos', 'Los prestamos se han cargado')
        except FileNotFoundError:
            QMessageBox.warning(self.new_window, 'Erro', 'El archivo no se ha encontrado')

    def save_data(self):
        with open('Save_loans.dat', 'wb') as file:
            pickle.dump(self.loans, file)
        QMessageBox.information(self.new_window, 'Guardar prestamos', 'Los prestamos se han guardado')






