from maquina_norma import ProcessadorNorma

def somar_valores(x, y):
    """
    Soma dois valores utilizando a máquina de Norma.

    Parâmetros:
        x (int): Primeiro valor a ser somado.
        y (int): Segundo valor a ser somado.

    Retorna:
        None
    """
    processador = ProcessadorNorma()
    processador.carregar_codigo("./operacoes/somar.txt")  # Carrega o código da soma
    processador.inicializar_registradores({'A': x, 'B': y, 'C': 0})  # Inicializa registradores
    processador.executar_codigo()  # Executa o código

    resultado = processador.registradores['A'].valor  # Resultado fica em A
    print(f"A soma de {x} + {y} é: {resultado}")

def produto_valores(x, y):
    """
    Multiplica dois valores utilizando a máquina de Norma.

    Parâmetros:
        x (int): Primeiro valor.
        y (int): Segundo valor.

    Retorna:
        None
    """
    processador = ProcessadorNorma()
    processador.carregar_codigo("./operacoes/multiplicar.txt")  # Carrega o código da multiplicação
    processador.inicializar_registradores({'A': x, 'B': y, 'C': 0, 'D': 0})  # Inicializa registradores
    processador.executar_codigo()  # Executa o código

    resultado = processador.registradores['A'].valor  # Resultado fica em A
    print(f"A multiplicação de {x} * {y} é: {resultado}")

def calcular_fatorial(valor):
    """
    Calcula o fatorial de um valor utilizando a máquina de Norma.

    Parâmetros:
        valor (int): Valor para calcular o fatorial.

    Retorna:
        None
    """
    if valor == 0:
        print(f"O fatorial de {valor} é: 1")
        return

    processador = ProcessadorNorma()
    processador.carregar_codigo("./operacoes/fatorial.txt")  # Carrega o código do fatorial
    processador.inicializar_registradores({'A': valor, 'B': 0, 'C': 0, 'D': 0})  # Inicializa registradores
    processador.executar_codigo()  # Executa o código

    resultado = processador.registradores['A'].valor  # Resultado fica em A
    print(f"O fatorial de {valor} é: {resultado}")

def comparar_menor(x, y):
    """
    Compara se x é menor que y utilizando a máquina de Norma.

    Parâmetros:
        x (int): Primeiro valor.
        y (int): Segundo valor.

    Retorna:
        None
    """
    processador = ProcessadorNorma()
    processador.carregar_codigo("./operacoes/a_b.txt")  # Carrega o código de comparação
    processador.inicializar_registradores({'A': x, 'B': y, 'C': 0, 'D': 0, 'E': 0})  # Inicializa registradores
    processador.executar_codigo()  # Executa o código

    # O resultado da comparação é armazenado no registrador E
    if processador.registradores['E'].valor > 0:
        print(f"{x} é menor que {y}.")
    else:
        print(f"{x} NÃO é menor que {y}.")

def menu_principal():
    """
    Exibe o menu principal e executa a operação escolhida pelo usuário.

    Retorna:
        None
    """
    print("Selecione a operação desejada:")
    print("1 - Somar dois valores")
    print("2 - Multiplicar dois valores")
    print("3 - Calcular fatorial")
    print("4 - Verificar se X < Y")
    print("0 - Encerrar")

    opcao = input("Informe a opção: ")

    if opcao == '1':
        x = int(input("Digite o valor de X: "))
        y = int(input("Digite o valor de Y: "))
        somar_valores(x, y)
    elif opcao == '2':
        x = int(input("Digite o valor de X: "))
        y = int(input("Digite o valor de Y: "))
        produto_valores(x, y)
    elif opcao == '3':
        valor = int(input("Digite o valor: "))
        calcular_fatorial(valor)
    elif opcao == '4':
        x = int(input("Digite o valor de X: "))
        y = int(input("Digite o valor de Y: "))
        comparar_menor(x, y)
    elif opcao == '0':
        print("Finalizando...")
        return
    else:
        print("Opção inválida!")

    print()
    menu_principal()  # Chama novamente o menu para nova operação

if __name__ == "__main__":
    # Ponto de entrada do programa
    menu_principal()
