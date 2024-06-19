# Bibliotecas
from PyQt5.QtCore import *  # Funções centrais
from PyQt5.QtWidgets import *  # Interface gráfica
from PyQt5.QtWebEngineWidgets import *
import sys  # Funções e variáveis do sistema
import random
import string


class GeradorDeSenhas:
    def __init__(self, tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
        """
        Inicializa o gerador de senhas com o tamanho e configurações especificadas.

        Parâmetros:
        tamanho (int): O tamanho da senha a ser gerada. Padrão é 12 caracteres.
        usar_maiusculas (bool): Incluir letras maiúsculas na senha. Padrão é True.
        usar_minusculas (bool): Incluir letras minúsculas na senha. Padrão é True.
        usar_numeros (bool): Incluir números na senha. Padrão é True.
        usar_simbolos (bool): Incluir símbolos na senha. Padrão é True.
        """
        self.tamanho = tamanho
        self.caracteres = ''
        if usar_maiusculas:
            self.caracteres += string.ascii_uppercase
        if usar_minusculas:
            self.caracteres += string.ascii_lowercase
        if usar_numeros:
            self.caracteres += string.digits
        if usar_simbolos:
            self.caracteres += string.punctuation

    def gerar_senha(self):
        """
        Gera uma senha aleatória com o tamanho e configurações especificadas no inicializador.

        Retorna:
        str: Uma senha aleatória.
        """
        if not self.caracteres:
            raise ValueError("Nenhum conjunto de caracteres selecionado para gerar a senha.")
        return ''.join(random.choice(self.caracteres) for _ in range(self.tamanho))


class GeradorDeSenhasUI(QDockWidget):
    def __init__(self, parent=None):
        super(GeradorDeSenhasUI, self).__init__("Gerador de Senhas", parent)

        # Widgets de entrada
        self.tamanho_input = QSpinBox()
        self.tamanho_input.setRange(1, 128)  # Definindo o intervalo do tamanho da senha
        self.tamanho_input.setValue(12)  # Tamanho padrão

        self.check_maiusculas = QCheckBox("Incluir letras maiúsculas")
        self.check_maiusculas.setChecked(True)
        self.check_minusculas = QCheckBox("Incluir letras minúsculas")
        self.check_minusculas.setChecked(True)
        self.check_numeros = QCheckBox("Incluir números")
        self.check_numeros.setChecked(True)
        self.check_simbolos = QCheckBox("Incluir símbolos")
        self.check_simbolos.setChecked(True)

        self.btn_gerar = QPushButton("Gerar Senha")
        self.btn_gerar.clicked.connect(self.gerar_senha)

        self.senha_output = QLineEdit()
        self.senha_output.setReadOnly(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Tamanho da Senha:"))
        layout.addWidget(self.tamanho_input)
        layout.addWidget(self.check_maiusculas)
        layout.addWidget(self.check_minusculas)
        layout.addWidget(self.check_numeros)
        layout.addWidget(self.check_simbolos)
        layout.addWidget(self.btn_gerar)
        layout.addWidget(QLabel("Senha Gerada:"))
        layout.addWidget(self.senha_output)

        # Configuração do widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setWidget(widget)

    def gerar_senha(self):
        tamanho = self.tamanho_input.value()
        usar_maiusculas = self.check_maiusculas.isChecked()
        usar_minusculas = self.check_minusculas.isChecked()
        usar_numeros = self.check_numeros.isChecked()
        usar_simbolos = self.check_simbolos.isChecked()

        try:
            gerador = GeradorDeSenhas(
                tamanho,
                usar_maiusculas,
                usar_minusculas,
                usar_numeros,
                usar_simbolos
            )
            senha_gerada = gerador.gerar_senha()
            self.senha_output.setText(senha_gerada)
        except ValueError as e:
            QMessageBox.warning(self, "Erro", str(e))


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
        self.gerador_senhas.hide()

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
