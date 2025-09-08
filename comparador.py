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

def mostrar_resultados(resultado_seq, comp_seq, tempo_seq, resultado_bin, comp_bin, tempo_bin_total):
    print("\nRESULTADOS DA BUSCA (COMPARAÇÃO JUSTA)\n")

    print("[ CENÁRIO 1: BUSCA SEQUENCIAL (em dados desordenados) ]")
    if resultado_seq:
        print(f"Elemento encontrado: {resultado_seq}")
    else:
        print("Elemento não encontrado.")
    print(f"Comparações: {comp_seq}")
    print(f"Tempo médio: {tempo_seq:.6f} ms\n")

    print("[ CENÁRIO 2: BUSCA BINÁRIA (incluindo tempo para ordenar) ]")
    if resultado_bin:
        print(f"Elemento encontrado: {resultado_bin}")
    else:
        print("Elemento não encontrado.")
    print(f"Comparações da busca: {comp_bin}")
    print(f"Tempo médio (Ordenação + Busca): {tempo_bin_total:.6f} ms\n")


def mostrar_grafico(comp_seq, tempo_seq, comp_bin, tempo_bin_total):
    plt.figure(figsize=(12, 5))
    plt.suptitle("Comparativo de Desempenho (Cenário de Busca Única)", fontsize=16)

    plt.subplot(1, 2, 1)
    plt.bar(['Sequencial', 'Binária'], [comp_seq, comp_bin], color=['orange', 'blue'])
    plt.title("Número de Comparações (Apenas a Busca)")
    plt.ylabel("Comparações")

    plt.subplot(1, 2, 2)
    labels = ['Sequencial', 'Binária + Ordenação']
    tempos = [tempo_seq, tempo_bin_total]
    plt.bar(labels, tempos, color=['orange', 'blue'])
    plt.title("Tempo de Execução Total")
    plt.ylabel("Tempo (ms)")

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    limpar_tela()
    arquivo = "dados.txt" 
    print(f"Carregando dados do arquivo '{arquivo}'...")
    dados = carregar_dados(arquivo)
    if not dados:
        print("Arquivo não encontrado ou vazio. Encerrando.")
        exit()
    print(f"Arquivo carregado com {len(dados)} registros.")

    chave = input("\nDigite o nome para buscar: ")
    limpar_tela()

    REPETICOES = 100

    print("Calculando tempo da Busca Sequencial...")
    inicio = time.perf_counter()
    for _ in range(REPETICOES):
        resultado_seq, comp_seq = busca_sequencial(dados, chave)
    fim = time.perf_counter()
    tempo_seq = (fim - inicio) / REPETICOES * 1000

    print("Calculando tempo da Busca Binária + Ordenação...")
    inicio = time.perf_counter()
    for _ in range(REPETICOES):
        dados_para_ordenar = list(dados)
        dados_para_ordenar.sort(key=lambda x: x[0])
        resultado_bin, comp_bin = busca_binaria(dados_para_ordenar, chave)
    fim = time.perf_counter()
    tempo_bin_com_ordenacao = (fim - inicio) / REPETICOES * 1000

    mostrar_resultados(resultado_seq, comp_seq, tempo_seq, resultado_bin, comp_bin, tempo_bin_com_ordenacao)
    mostrar_grafico(comp_seq, tempo_seq, comp_bin, tempo_bin_com_ordenacao)