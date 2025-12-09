import matplotlib.pyplot as plt

# =================================================================
# DADOS DE ENTRADA PARA A GERAÇÃO DO GRÁFICO (TÓPICO 2.3)
# ATENÇÃO: Estes dados DEVEM ser substituídos pelos resultados reais do Tópico 2.2.
# =================================================================

# Eixo X: Tamanhos de entrada testados (Número de elementos N)
tamanhos_de_entrada = [100, 1_000, 10_000, 50_000, 100_000, 500_000, 1_000_000]

# Eixo Y: Tempos de execução em milissegundos para a ordenação Crescente
# A complexidade O(N) sugere que esta linha será quase perfeitamente linear.
tempo_ms_crescente = [0.015, 0.08, 0.75, 3.80, 7.50, 38.00, 75.00] 

# Eixo Y: Tempos de execução em milissegundos para a ordenação Decrescente
# O Radix Sort deve ter tempos muito próximos ao Crescente, validando a complexidade O(N) 
# (independente do caso: melhor ou pior).
tempo_ms_decrescente = [0.017, 0.09, 0.76, 3.90, 7.60, 38.50, 75.50] 

# =================================================================
# FUNÇÃO DE GERAÇÃO E CONFIGURAÇÃO DO GRÁFICO (REQUISITO 2.3)
# =================================================================

def gerar_grafico_radix_sort_comparativo(tamanhos, tempo_cres, tempo_decr):
    
    # Define o tamanho da figura (largura x altura em polegadas) para melhor visualização
    plt.figure(figsize=(10, 6))
    
    # 1. PLOTAGEM DAS DUAS SÉRIES DE DADOS
    
    # Plota o tempo para ordenação Crescente
    plt.plot(tamanhos, tempo_cres, 
             label='Ordenação Crescente',  # Rótulo para a legenda
             marker='o', linestyle='-', color='blue', linewidth=2) # Configurações visuais

    # Plota o tempo para ordenação Decrescente (comparação do Pior Caso)
    plt.plot(tamanhos, tempo_decr, 
             label='Ordenação Decrescente', 
             marker='x', linestyle='--', color='red', linewidth=2)

    # 2. CONFIGURAÇÕES E RÓTULOS (CONFORME REQUISITOS DO PROJETO 2.3)
    
    # Título do Gráfico (Requisito 2.3)
    plt.title('Desempenho do Radix Sort: Comparação Crescente vs. Decrescente', 
              fontsize=15, fontweight='bold')
    
    # Rótulo do Eixo X (Tamanho da Entrada) (Requisito 2.3)
    plt.xlabel('Tamanho da Entrada (Nº de Elementos)', fontsize=12)
    
    # Rótulo do Eixo Y (Tempo em Milissegundos) (Requisito 2.3)
    plt.ylabel('Tempo de Execução (ms)', fontsize=12)
    
    # Legenda (Requisito 2.3) - Essencial para diferenciar as duas curvas
    plt.legend(fontsize=10)
    
    # Adiciona a grade ao gráfico para facilitar a leitura dos valores
    plt.grid(True, linestyle=':', alpha=0.7)
    
    # Formata os rótulos do eixo X para não usarem notação científica (mantém o formato '1,000,000')
    plt.ticklabel_format(style='plain', axis='x', useOffset=False)
    
    # Define o limite do eixo X para começar em 0 (melhora a visualização da origem)
    plt.xlim(left=0) 
    
    # Ajusta o layout para evitar que rótulos sejam cortados
    plt.tight_layout()
    
    # Exibe o gráfico gerado
    plt.show()

# =================================================================
# EXECUÇÃO
# =================================================================
if __name__ == '__main__':
    # Chama a função para gerar o gráfico usando os dados definidos acima
    gerar_grafico_radix_sort_comparativo(tamanhos_de_entrada, tempo_ms_crescente, tempo_ms_decrescente)
