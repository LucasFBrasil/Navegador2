# gerador_de_senhas.py

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
