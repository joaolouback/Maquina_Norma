import os

def inicializar_registradores_personalizado():
    registradores = {}
    print("\n--- Inicialização dos Registradores ---")
    while True:
        try:
            n = int(input("Quantos registradores deseja usar? (1 a 8): "))
            if 1 <= n <= 8:
                break
            else:
                print("Digite um número entre 1 e 8.")
        except ValueError:
            print("Digite um número válido.")

    lista_registradores = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'][:n]

    for r in lista_registradores:
        while True:
            try:
                val = int(input(f"Valor inicial para {r}: "))
                registradores[r] = val
                break
            except ValueError:
                print("Digite um número inteiro.")

    # Inicializa os demais com 0 para manter compatibilidade
    for r in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        if r not in registradores:
            registradores[r] = 0

    return registradores, lista_registradores

def exibir_estado(registradores, linha_atual, instrucao, usados):
    estado = tuple(registradores[r] for r in usados)
    print(f"{estado} , {linha_atual}) {instrucao}")

def interpretar_instrucao(linha):
    rotulo, instr = linha.split(':')
    rotulo = int(rotulo.strip())
    instr = instr.strip()
    partes = instr.split()

    if len(partes) == 3 and partes[0] == "ADD":
        return rotulo, ("ADD", partes[1], int(partes[2]))
    elif len(partes) == 3 and partes[0] == "SUB":
        return rotulo, ("SUB", partes[1], int(partes[2]))
    elif len(partes) == 4 and partes[0] == "ZER":
        return rotulo, ("ZER", partes[1], int(partes[2]), int(partes[3]))
    else:
        raise ValueError(f"Instrução inválida: {instr}")

def ler_programa(caminho):
    if not os.path.exists(caminho):
        print("Arquivo não encontrado.")
        return None
    programa = {}
    with open(caminho, 'r') as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                try:
                    rotulo, dados = interpretar_instrucao(linha)
                    programa[rotulo] = dados
                except Exception as e:
                    print(f"Erro ao ler linha: {linha}\n{e}")
    return programa

def executar_programa(programa, registradores, usados):
    if not programa:
        print("Nenhum programa carregado.")
        return

    print("\n--- Execução Iniciada ---\n")
    print("Valores iniciais dos registradores:")
    estado = tuple(registradores[r] for r in usados)
    print(f"{estado} , M) Entrada de Dados")

    linha_atual = min(programa.keys())

    while linha_atual in programa:
        instrucao = programa[linha_atual]
        op = instrucao[0]
        reg = instrucao[1]

        if op == "ADD":
            prox = instrucao[2]
            registradores[reg] += 1
            exibir_estado(registradores, linha_atual, f"FACA ADD ({reg}) VA_PARA {prox}", usados)
            linha_atual = prox

        elif op == "SUB":
            prox = instrucao[2]
            if registradores[reg] > 0:
                registradores[reg] -= 1
            exibir_estado(registradores, linha_atual, f"FACA SUB ({reg}) VA_PARA {prox}", usados)
            linha_atual = prox

        elif op == "ZER":
            destino_zero, destino_nzero = instrucao[2], instrucao[3]
            proxima = destino_zero if registradores[reg] == 0 else destino_nzero
            exibir_estado(registradores, linha_atual, f"SE ZER ({reg}) ENTAO VA_PARA {destino_zero} SENAO VA_PARA {destino_nzero}", usados)
            linha_atual = proxima

        else:
            print(f"Instrução desconhecida: {instrucao}")
            break

    print("\n--- Programa encerrado ---")

def mostrar_registradores(registradores, usados):
    print("\nEstado atual dos registradores:")
    for r in usados:
        print(f"{r} = {registradores.get(r, 0)}", end="  ")
    print("\n")

def menu():
    registradores = None
    programa = None
    usados = []

    while True:
        print("\n======= MÁQUINA NORMA =======")
        print("1 - Inicializar registradores")
        print("2 - Carregar programa (.txt)")
        print("3 - Exibir registradores")
        print("4 - Executar programa")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registradores, usados = inicializar_registradores_personalizado()
        elif opcao == '2':
            caminho = input("Digite o caminho do arquivo .txt: ")
            programa = ler_programa(caminho)
            if programa:
                print("Programa carregado com sucesso.")
        elif opcao == '3':
            if registradores:
                mostrar_registradores(registradores, usados)
            else:
                print("Inicialize os registradores primeiro.")
        elif opcao == '4':
            if not registradores:
                print("Inicialize os registradores primeiro.")
            elif not programa:
                print("Carregue um programa primeiro.")
            else:
                executar_programa(programa, registradores, usados)
        elif opcao == '5':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()