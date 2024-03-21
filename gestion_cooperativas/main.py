import sys
import random
import pickle
from PyQt5.QtWidgets import QApplication
from loginwindow import VentanaLogin
from list import List
from usuario import Usuario
usuarios = List()
# value = random.randint(1000, 9999)
# value2 = random.randint(1000, 9999)
# usuario1 = Usuario('admin', 'admin', str(value), 'Francisco Isaac Gudiel Quemé',
#                    'Gerente', 'Activo')
# usuarios.append(usuario1)


usuarios_cargados = []
with open("objetos.txt", "rb") as archivo:
    try:
        while True:
            objeto = pickle.load(archivo)
            usuarios_cargados.append(objeto)
    except EOFError:
        pass

# Subir a usuarios los usuarios cargados
for user in usuarios_cargados:
    usuarios.append(user)


def main():
    app = QApplication(sys.argv)
    ventana_login = VentanaLogin(usuarios, app)
    ventana_login.show()

    sys.exit(app.exec())


main()
