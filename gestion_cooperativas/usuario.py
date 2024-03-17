class Usuario:
    def __init__(self, email: str, password: str, usercode: str, name: str, job: str, status: str):
        self.email = email
        self.password = password
        self.usercode = usercode
        self.name = name
        self.job = job
        self.status = status

    def __str__(self):
        valor = f'Nombre: {self.name}\nCódigo: {self.usercode}\nPuesto: {self.job}\nEstado: {self.status}'
        return valor
