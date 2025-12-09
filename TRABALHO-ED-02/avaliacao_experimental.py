import time
import random

# Este script executa a Avaliação Experimental (Tópico 2.2), medindo o tempo 
# de execução do Radix Sort para diferentes tamanhos de entrada (N).

# --- FUNÇÕES AUXILIARES ---

def gerar_lista_inteiros_positivos(tamanho):
    """
    Função de suporte para gerar uma lista de inteiros positivos aleatórios.
    Esta lista representa o "Caso Médio" (lista aleatória) para os testes.
    Os números são gerados no intervalo [1, 100000].
    """
    # A função random.randint é usada para gerar números inteiros aleatórios no intervalo especificado.
    return [random.randint(1, 100000) for _ in range(tamanho)]

# IMPORTANTE: A função radix_sort_int DEVE ser importada ou definida neste arquivo 
# para que os testes funcionem. Ela deve vir do seu código do Tópico 2.1.
# Exemplo (remover o comentário SE você não tiver importado):
# def radix_sort_int(lista, crescente=True):
#     ... (implementação completa do Radix Sort para inteiros) ...


def realizar_teste_de_complexidade_int():
    """
    Função principal para executar os testes de complexidade e gerar a tabela de resultados.
    """
    
    # Tamanhos de entrada a serem testados (do menor ao maior) (Requisito 2.2)
    # A progressão garante que o comportamento O(N) seja claramente visível.
    tamanhos_de_entrada = [100, 1_000, 10_000, 50_000, 100_000, 500_000, 1_000_000]
    
    # Dicionário para armazenar os resultados que serão exportados para o gráfico.
    resultados = {
        'Tamanho (N)': [],
        'Tempo (ms) - Crescente': [],
        'Tempo (ms) - Decrescente': []
    }
    
    print("--- Iniciando Testes de Complexidade do Radix Sort (Inteiros) ---")
    
    # Loop principal: itera sobre cada tamanho de entrada (N)
    for N in tamanhos_de_entrada:
        print(f"\nTestando N = {N:,} elementos...")
        
        # Geramos a lista aleatória para garantir que o tempo de ordenação seja consistente.
        lista_original = gerar_lista_inteiros_positivos(N)
        
        # --- TESTE 1: ORDENAÇÃO CRESCENTE (Melhor ou Caso Médio) ---
        # Usamos uma cópia para não alterar a lista original para o próximo teste
        lista_crescente = lista_original.copy()
        
        # Medição de tempo: time.perf_counter() é recomendado para medições precisas de benchmark.
        tempo_inicio_cres = time.perf_counter()
        radix_sort_int(lista_crescente, crescente=True) # Chama o algoritmo
        tempo_ms_crescente = (time.perf_counter() - tempo_inicio_cres) * 1000 # Converte para milissegundos
        print(f"  - Tempo Crescente: {tempo_ms_crescente:.4f} ms")
        
        # --- TESTE 2: ORDENAÇÃO DECRESCENTE (Comparação com o Pior Caso) ---
        # Este teste verifica se o Pior Caso (reverso) do Radix Sort é diferente do Melhor Caso.
        lista_decrescente = lista_original.copy()
        tempo_inicio_decr = time.perf_counter()
        radix_sort_int(lista_decrescente, crescente=False) # Chama o algoritmo (modo decrescente)
        tempo_ms_decrescente = (time.perf_counter() - tempo_inicio_decr) * 1000
        print(f"  - Tempo Decrescente: {tempo_ms_decrescente:.4f} ms")
        
        # Armazenar Resultados na tabela
        resultados['Tamanho (N)'].append(N)
        resultados['Tempo (ms) - Crescente'].append(tempo_ms_crescente)
        resultados['Tempo (ms) - Decrescente'].append(tempo_ms_decrescente)

    
    # ------------------- APRESENTAÇÃO DA TABELA (REQUISITO 2.3) -------------------
    print("\n\n--- TABELA DE TESTES DO RADIX SORT (Inteiros) ---")
    
    # Impressão do Cabeçalho da tabela em formato Markdown/ASCII
    print("| Tamanho (N) | Tempo (ms) - Crescente | Tempo (ms) - Decrescente |")
    print("|-------------|------------------------|--------------------------|")
    
    # Impressão das Linhas de Dados
    for i in range(len(tamanhos_de_entrada)):
        tamanho = resultados['Tamanho (N)'][i]
        tempo_cres = resultados['Tempo (ms) - Crescente'][i]
        tempo_decr = resultados['Tempo (ms) - Decrescente'][i]
        
        # Formatação garante alinhamento e 4 casas decimais para o tempo
        print(f"| {tamanho:11,} | {tempo_cres:22.4f} | {tempo_decr:24.4f} |")
        
    # Retorna o dicionário para ser usado como entrada no script de geração de gráfico (Tópico 2.3)
    return resultados

if __name__ == '__main__':
    # Bloco de execução principal: inicia os testes e armazena os dados
    # A função radix_sort_int deve estar acessível neste ponto.
    dados_para_grafico = realizar_teste_de_complexidade_int()
