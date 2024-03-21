import random

class Loan:
    def __init__(self, user, user_code, money, reason, month_income, warranty, plan_pay, record: str):
        self.user1 = user
        self.code1 = str(random.randint(1000, 9999))
        self.user_code1 = user_code
        self.status1 = 'Creado'
        self.money1 = money
        self.pay_act1 = money
        self.amount_approved1 = reason
        self.month_income1 = month_income
        self.warranty1 = warranty
        self.plan_pay1 = plan_pay
        self.pay_record1 = record
