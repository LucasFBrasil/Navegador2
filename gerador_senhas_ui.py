# gerador_de_senhas_ui.py

from PyQt5.QtWidgets import *
from gerador_senhas import GeradorDeSenhas

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
