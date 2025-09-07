import time
import os
import matplotlib.pyplot as plt

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def carregar_dados(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        dados = [linha.strip().split(",") for linha in f.readlines()]
    return dados

def busca_sequencial(vetor, chave):
    comparacoes = 0
    for i in range(len(vetor)):
        comparacoes += 1
        if vetor[i][0] == chave:
            return (vetor[i], comparacoes)
    return (None, comparacoes)

def busca_binaria(vetor, chave):
    comparacoes = 0
    inferior, superior = 0, len(vetor) - 1
    while inferior <= superior:
        meio = (inferior + superior) // 2
        comparacoes += 1
        if vetor[meio][0] == chave:
            return (vetor[meio], comparacoes)
        elif chave < vetor[meio][0]:
            superior = meio - 1
        else:
            inferior = meio + 1
    return (None, comparacoes)

def mostrar_resultados(resultado_seq, comp_seq, tempo_seq, resultado_bin, comp_bin, tempo_bin):
    print("\nRESULTADOS DA BUSCA\n")

    print("[ BUSCA SEQUENCIAL ]")
    if resultado_seq:
        print(f"Elemento encontrado: {resultado_seq}")
    else:
        print("Elemento não encontrado.")
    print(f"Comparações: {comp_seq}")
    print(f"Tempo médio: {tempo_seq:.6f} ms\n")

    print("[ BUSCA BINÁRIA ]")
    if resultado_bin:
        print(f"Elemento encontrado: {resultado_bin}")
    else:
        print("Elemento não encontrado.")
    print(f"Comparações: {comp_bin}")
    print(f"Tempo médio: {tempo_bin:.6f} ms\n")

    print("[ COMPARAÇÃO DE EFICIÊNCIA ]")
    if comp_seq > comp_bin:
        print(f"A busca sequencial fez {comp_seq - comp_bin} comparações a mais que a binária.")
    elif comp_bin > comp_seq:
        print(f"A busca binária fez {comp_bin - comp_seq} comparações a mais que a sequencial.")
    else:
        print("As duas buscas fizeram o mesmo número de comparações.")

def mostrar_grafico(comp_seq, tempo_seq, comp_bin, tempo_bin):
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.bar(['Sequencial', 'Binária'], [comp_seq, comp_bin], color=['orange', 'blue'])
    plt.title("Número de Comparações")
    plt.ylabel("Comparações")

    plt.subplot(1, 2, 2)
    plt.bar(['Sequencial', 'Binária'], [tempo_seq, tempo_bin], color=['orange', 'blue'])
    plt.title("Tempo Médio (ms)")
    plt.ylabel("Tempo (ms)")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    limpar_tela()
    arquivo = "dados.txt"
    print(f"Carregando dados do arquivo '{arquivo}'...")
    dados = carregar_dados(arquivo)
    print(f"Arquivo carregado com {len(dados)} registros.")

    escolha = input("Deseja ordenar os dados antes da busca? (s/n): ").strip().lower()
    if escolha == 's':
        inicio = time.perf_counter()
        dados.sort(key=lambda x: x[0])
        fim = time.perf_counter()
        print(f"Dados ordenados. Tempo para ordenação: {(fim - inicio) * 1000:.4f} ms")
    else:
        print("Dados mantidos bagunçados. A busca binária pode não funcionar corretamente.")

    chave = input("\nDigite o nome para buscar: ")
    limpar_tela()  # limpa a tela após digitar o nome

    REPETICOES = 1000

    inicio = time.perf_counter()
    for _ in range(REPETICOES):
        resultado_seq, comp_seq = busca_sequencial(dados, chave)
    fim = time.perf_counter()
    tempo_seq = (fim - inicio) / REPETICOES * 1000

    inicio = time.perf_counter()
    for _ in range(REPETICOES):
        resultado_bin, comp_bin = busca_binaria(dados, chave)
    fim = time.perf_counter()
    tempo_bin = (fim - inicio) / REPETICOES * 1000

    mostrar_resultados(resultado_seq, comp_seq, tempo_seq, resultado_bin, comp_bin, tempo_bin)
    mostrar_grafico(comp_seq, tempo_seq, comp_bin, tempo_bin)
