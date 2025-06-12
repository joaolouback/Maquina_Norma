class Comando:
    """
    Classe que representa um comando (instrução) da Máquina de Norma.
    Cada comando possui um rótulo, uma operação (ADD, SUB, ZER),
    um registrador alvo, o próximo rótulo e, opcionalmente, um rótulo alternativo.
    """

    def __init__(self, rotulo, operacao, registrador, proximo, alternativo=None):
        """
        Inicializa um comando da Máquina de Norma.

        Parâmetros:
            rotulo (int): Rótulo numérico da instrução.
            operacao (str): Operação a ser executada (ADD, SUB, ZER).
            registrador (str): Registrador alvo (A-H).
            proximo (int): Próximo rótulo a ser executado.
            alternativo (int, opcional): Rótulo alternativo (usado em ZER).
        """
        self.rotulo = rotulo
        self.operacao = operacao
        self.registrador = registrador
        self.proximo = proximo
        self.alternativo = alternativo

    def executar(self, registradores):
        """
        Executa a operação do comando sobre o registrador indicado.

        Parâmetros:
            registradores (dict): Dicionário de registradores (A-H).

        Retorna:
            int or None: Próxima posição/rótulo a ser executado, ou None para encerrar.
        """
        match self.operacao:
            case "ADD":
                # Incrementa o valor do registrador em 1
                registradores[self.registrador].aumentar()
                return self.proximo
            case "SUB":
                # Decrementa o valor do registrador em 1 (se possível)
                registradores[self.registrador].reduzir()
                return self.proximo
            case "ZER":
                # Verifica se o registrador está vazio (zero)
                if registradores[self.registrador].esta_vazio():
                    return self.proximo
                else:
                    return self.alternativo
            case _:
                # Operação desconhecida, encerra execução
                return None

    def __str__(self):
        """
        Retorna uma representação textual do comando.

        Retorna:
            str: Representação da instrução no formato original.
        """
        return f"{self.rotulo}: {self.operacao} {self.registrador} {self.proximo} {'' if self.alternativo is None else self.alternativo}"
