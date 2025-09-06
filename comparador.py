import random

def gerar_dados(tamanho_vetor):
    """
    Gera uma lista ordenada de números para servir como base de dados.
    """
    print(f"Gerando um vetor ordenado de {tamanho_vetor} elementos...")
    # Gera uma sequência de números, por exemplo, de 0 a tamanho_vetor - 1
    vetor = list(range(tamanho_vetor))
    print("Vetor gerado com sucesso!")
    return vetor

def busca_sequencial(vetor, chave):
    """
    Realiza a busca sequencial em um vetor.
    """
    comparacoes = 0
    # Percorre o vetor do início ao fim
    for i in range(len(vetor)):
        comparacoes += 1 # Conta cada verificação
        if vetor[i] == chave:
            return (i, comparacoes) # Chave encontrada, retorna a posição e as comparações
    
    return (-1, comparacoes) # Chave não encontrada após percorrer todo o vetor

def busca_binaria(vetor, chave):
    """
    Realiza a busca binária em um vetor ordenado.
    """
    comparacoes = 0
    inferior = 0
    superior = len(vetor) - 1

    while inferior <= superior:
        meio = (inferior + superior) // 2
        comparacoes += 1 # Conta a comparação principal

        if vetor[meio] == chave:
            return (meio, comparacoes) # Chave encontrada
        
        # Compara para decidir qual metade descartar
        elif chave < vetor[meio]:
            superior = meio - 1 # Busca na metade inferior
        else:
            inferior = meio + 1 # Busca na metade superior
            
    return (-1, comparacoes) # Chave não encontrada

if __name__ == "__main__":
    TAMANHO_VETOR = 20000 # Aumente este valor para ver uma diferença maior!
    
    # Gera os dados
    meu_vetor = gerar_dados(TAMANHO_VETOR)
    
    # Pede ao usuário um número para buscar
    try:
        chave_busca = int(input("Digite um número para buscar no vetor: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        exit()

    print(f"\nBuscando pelo número {chave_busca} em um vetor de {TAMANHO_VETOR} elementos...\n")

    # 3. Executa e cronometra a Busca Sequencial
    pos_seq, comp_seq = busca_sequencial(meu_vetor, chave_busca)
    
    print("--- Resultado da Busca Sequencial ---")
    if pos_seq != -1:
        print(f"Elemento encontrado na posição: {pos_seq}")
    else:
        print("Elemento não encontrado.")
    print(f"Número de comparações: {comp_seq}")

    # 4. Executa e cronometra a Busca Binária
    pos_bin, comp_bin = busca_binaria(meu_vetor, chave_busca)
    
    print("\n--- Resultado da Busca Binária ---")
    if pos_bin != -1:
        print(f"Elemento encontrado na posição: {pos_bin}")
    else:
        print("Elemento não encontrado.")
    print(f"Número de comparações: {comp_bin}")

    # 5. Conclusão
    print("\n--- Conclusão ---")
    if comp_bin > 0 and comp_seq > comp_bin:
        diferenca = round(comp_seq / comp_bin)
        print(f"A Busca Binária foi aproximadamente {diferenca}x mais rápida que a Busca Sequencial.")
    else:
        print("Não foi possível calcular a diferença de performance.")