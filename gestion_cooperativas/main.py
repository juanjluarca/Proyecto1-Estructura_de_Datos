import sys
import random
from PyQt5.QtWidgets import QApplication
from loginwindow import VentanaLogin
from list import List
from usuario import Usuario
usuarios = List()
value = random.randint(1000, 9999)
value2 = random.randint(1000, 9999)
usuario1 = Usuario('admin', 'admin', str(value), 'Francisco Isaac Gudiel Quemé',
                   'Gerente', 'Activo')
usuario2 = Usuario('example', 'example', str(value2), 'Jorge Escalante', 'Coordinador',
                   'Inactivo')
usuarios.append(usuario1)
usuarios.append(usuario2)


def main():
    app = QApplication(sys.argv)
    ventana_login = VentanaLogin(usuarios, app)
    ventana_login.show()
    sys.exit(app.exec())


main()
