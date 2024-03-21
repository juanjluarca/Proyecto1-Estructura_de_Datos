import random
class Loan:
    def __init__(self, user, user_code, money, reason, month_income, warranty, plan_pay, record):
        self.user = user
        self.code = str(random.randint(1000, 9999))
        self.user_code = user_code
        self.status = 'Creado'
        self.money = money
        self.number_pay = plan_pay
        self.amount_approved = reason
        self.month_income = month_income
        self.warranty = warranty
        self.plan_pay = plan_pay
        self.pay_record = record

    def __str__(self):
        result = (f'Cantidad del prestamo actual {self.money}\n'
                  f'Numeros de pagos realizados {len(self.pay_record)}\n'
                  f'Estado del prestamo {self.status}\n'
                  f'Nombre del usuario que realizo el prestamo {self.user.name}\n'
                  f'Ingresos mensuales del usuario {self.month_income}\n'
                  f'El lapso de tiempo de pago es de {self.plan_pay}')

        return result
