import re
from instrucoes import Comando
from registrador import Acumulador

class ProcessadorNorma:
    """
    Classe que simula o processador da Máquina de Norma.
    Responsável por carregar, inicializar e executar instruções
    em um conjunto de registradores simulados.
    """

    def __init__(self):
        """
        Inicializa o processador com 8 registradores (A até H),
        um dicionário para armazenar o código (instruções)
        e define a posição inicial de execução.
        """
        # Inicializa registradores de A até H (A, B, C, ..., H)
        self.registradores = {chr(65 + i): Acumulador() for i in range(8)}
        self.codigo = {}  # Mapeamento: rótulo -> Comando
        self.posicao = 1  # Inicia na primeira instrução

    def carregar_codigo(self, arquivo_nome):
        """
        Carrega o código da Máquina de Norma a partir de um arquivo texto.

        Parâmetros:
            arquivo_nome (str): Caminho do arquivo contendo as instruções.

        Retorna:
            None
        """
        self.codigo = {}
        with open(arquivo_nome, "r") as arq:
            # Expressão regular para capturar instruções no formato esperado
            padrao = r"^(\d+):\s*([A-Z]{3})\s*([A-H])\s*(\d+)\s*(\d+)?$"
            conteudo = arq.read()
            comandos = re.findall(padrao, conteudo, re.MULTILINE)
            for cmd in comandos:
                rotulo, operacao, reg, prox, alt = cmd
                rotulo = int(rotulo)
                prox = int(prox)
                alt = int(alt) if alt and alt.strip() else None
                # Cria e armazena o comando no dicionário de código
                self.codigo[rotulo] = Comando(rotulo, operacao, reg, prox, alt)

    def inicializar_registradores(self, valores_iniciais):
        """
        Inicializa os registradores com valores fornecidos.

        Parâmetros:
            valores_iniciais (dict): Dicionário com os valores iniciais para cada registrador.

        Retorna:
            None
        """
        for reg in self.registradores:
            if reg in valores_iniciais:
                self.registradores[reg].valor = valores_iniciais[reg]
            else:
                self.registradores[reg].valor = 0

    def executar_codigo(self):
        """
        Executa as instruções carregadas na máquina de Norma,
        começando da posição inicial até o fim do código.

        Retorna:
            None
        """
        print(self)  # Exibe o estado inicial dos registradores
        while self.posicao is not None:
            if self.posicao not in self.codigo:
                print(f"Execução encerrada: instrução {self.posicao} não localizada.")
                break
            comando = self.codigo[self.posicao]
            self.posicao = comando.executar(self.registradores)
            print(self)  # Exibe o estado após cada instrução

    def __str__(self):
        """
        Retorna uma string representando o estado atual dos registradores,
        a posição de execução e a instrução atual.

        Retorna:
            str: Estado dos registradores e instrução atual.
        """
        estado_regs = {r: self.registradores[r].valor for r in self.registradores}
        instrucao_atual = self.codigo[self.posicao] if self.posicao in self.codigo else None
        return f"Registradores: {estado_regs} | Posição: {self.posicao} | Comando: {instrucao_atual}"
