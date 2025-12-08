import matplotlib.pyplot as plt

# --- DADOS DE EXEMPLO (SUBSTITUA PELOS DADOS REAIS DO TÓPICO 2.2!) ---

# Tamanhos de entrada (Eixo X)
tamanhos_de_entrada = [100, 1_000, 10_000, 50_000, 100_000, 500_000, 1_000_000]

# Tempos em milissegundos (Eixo Y) - Substitua pelos seus dados reais!
# Simulação de O(n*k), onde os tempos são muito próximos
tempo_ms_crescente = [0.015, 0.08, 0.75, 3.80, 7.50, 38.00, 75.00] 
tempo_ms_decrescente = [0.017, 0.09, 0.76, 3.90, 7.60, 38.50, 75.50] 

# --- FUNÇÃO DE GERAÇÃO DE GRÁFICO ---

def gerar_grafico_radix_sort_comparativo(tamanhos, tempo_cres, tempo_decr):
    
    plt.figure(figsize=(10, 6))
    
    # 1. Plotar os dados
    
    # Plota o tempo para ordenação Crescente
    plt.plot(tamanhos, tempo_cres, 
             label='Ordenação Crescente', 
             marker='o', linestyle='-', color='blue', linewidth=2)

    # Plota o tempo para ordenação Decrescente
    plt.plot(tamanhos, tempo_decr, 
             label='Ordenação Decrescente', 
             marker='x', linestyle='--', color='red', linewidth=2)

    # 2. Configurações e Rótulos (Requisitos 2.3)
    
    # Título (Requisito)
    plt.title('Desempenho do Radix Sort: Comparação Crescente vs. Decrescente', 
              fontsize=15, fontweight='bold')
    
    # Eixo X Rotulado (Requisito)
    plt.xlabel('Tamanho da Entrada (Nº de Elementos)', fontsize=12)
    
    # Eixo Y Rotulado (Requisito)
    plt.ylabel('Tempo de Execução (ms)', fontsize=12)
    
    # Legenda (Requisito) - Crucial para diferenciar as curvas
    plt.legend(fontsize=10)
    
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.ticklabel_format(style='plain', axis='x', useOffset=False)
    plt.xlim(left=0) 
    plt.tight_layout()
    
    # Exibe o gráfico
    plt.show()

# --- Execução ---
if __name__ == '__main__':
    gerar_grafico_radix_sort_comparativo(tamanhos_de_entrada, tempo_ms_crescente, tempo_ms_decrescente)