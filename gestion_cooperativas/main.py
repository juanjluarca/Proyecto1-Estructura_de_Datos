import sys
import random
import pickle
from PyQt5.QtWidgets import QApplication
from loginwindow import VentanaLogin
from list import List
from usuario import Usuario

usuarios = List()
asociados = List()


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
