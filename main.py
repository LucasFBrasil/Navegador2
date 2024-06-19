# main.py
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
from gerador_senhas_ui import GeradorDeSenhasUI


class NavegadorPY(QMainWindow):
    def __init__(self, *args, **kwargs):  # Método inicializador
        super(NavegadorPY, self).__init__(*args, **kwargs)  # Inicializador da classe

        self.setWindowTitle("NavegadorPY")  # Nome da janela

        self.showMaximized()  # Janela Maximizada

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))  # URL principal

        self.setCentralWidget(self.browser)

        # Adicionando a interface de geração de senha
        self.gerador_senhas = GeradorDeSenhasUI(self)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.gerador_senhas)
        self.gerador_senhas.hide()  # Esconde o gerador de senhas inicialmente

        # Criando o menu
        self.menu = self.menuBar().addMenu("&Extensões")
        self.toggle_gerador_action = QAction("Gerador de Senhas", self)
        self.toggle_gerador_action.triggered.connect(self.toggle_gerador)
        self.menu.addAction(self.toggle_gerador_action)

    def toggle_gerador(self):
        if self.gerador_senhas.isVisible():
            self.gerador_senhas.hide()
        else:
            self.gerador_senhas.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NavegadorPY()  # Instancia
    app.exec()
