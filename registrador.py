class Acumulador:
    """
    Classe que representa um registrador acumulador da Máquina de Norma.
    Responsável por armazenar um valor inteiro não-negativo e fornecer
    operações básicas de incremento, decremento e verificação de vazio.
    """

    def __init__(self, valor=0):
        """
        Inicializa o acumulador com um valor não-negativo.

        Parâmetros:
            valor (int): Valor inicial do acumulador (padrão: 0).
        """
        self.valor = 0 if valor < 0 else valor  # Garante valor não-negativo

    def aumentar(self):
        """
        Incrementa o valor do acumulador em 1.
        """
        self.valor += 1  # Soma 1 ao valor

    def reduzir(self):
        """
        Decrementa o valor do acumulador em 1, se não estiver vazio.
        Não permite que o valor fique negativo.
        """
        if self.esta_vazio():
            return
        self.valor -= 1  # Subtrai 1 do valor

    def esta_vazio(self):
        """
        Verifica se o acumulador está vazio (valor igual a zero).

        Retorna:
            bool: True se valor for zero, False caso contrário.
        """
        return self.valor == 0  # Retorna True se valor for zero
