import time
import random

# --- FUNÇÕES AUXILIARES ---
# Estas funções devem vir do seu código do Tópico 2.1
def gerar_lista_inteiros_positivos(tamanho):
    """Gera uma lista de inteiros positivos aleatórios."""
    return [random.randint(1, 100000) for _ in range(tamanho)]

# Importe ou redefina aqui a função radix_sort_int do seu Tópico 2.1
# Exemplo (remova se já importou):
# def radix_sort_int(lista, crescente=True):
#     ... (implementação completa do Radix Sort para inteiros) ...


def realizar_teste_de_complexidade_int():
    
    # Tamanhos de entrada a serem testados (do menor ao maior)
    tamanhos_de_entrada = [100, 1_000, 10_000, 50_000, 100_000, 500_000, 1_000_000]
    
    # Tabela de resultados (focada em inteiros)
    resultados = {
        'Tamanho (N)': [],
        'Tempo (ms) - Crescente': [],
        'Tempo (ms) - Decrescente': []
    }
    
    print("--- Iniciando Testes de Complexidade do Radix Sort (Inteiros) ---")
    
    for N in tamanhos_de_entrada:
        print(f"\nTestando N = {N:,} elementos...")
        
        # Geramos a lista aleatória, que representa o "Caso Médio"
        lista_original = gerar_lista_inteiros_positivos(N)
        
        # --- TESTE 1: ORDENAÇÃO CRESCENTE ---
        # Usamos uma cópia para garantir que a lista_original possa ser usada novamente
        lista_crescente = lista_original.copy()
        tempo_inicio_cres = time.perf_counter()
        radix_sort_int(lista_crescente, crescente=True) 
        tempo_ms_crescente = (time.perf_counter() - tempo_inicio_cres) * 1000
        print(f"  - Tempo Crescente: {tempo_ms_crescente:.4f} ms")
        
        # --- TESTE 2: ORDENAÇÃO DECRESCENTE ---
        lista_decrescente = lista_original.copy()
        tempo_inicio_decr = time.perf_counter()
        radix_sort_int(lista_decrescente, crescente=False)
        tempo_ms_decrescente = (time.perf_counter() - tempo_inicio_decr) * 1000
        print(f"  - Tempo Decrescente: {tempo_ms_decrescente:.4f} ms")
        
        # Armazenar Resultados
        resultados['Tamanho (N)'].append(N)
        resultados['Tempo (ms) - Crescente'].append(tempo_ms_crescente)
        resultados['Tempo (ms) - Decrescente'].append(tempo_ms_decrescente)

    
    # ------------------- APRESENTAÇÃO DA TABELA (REQUISITO) -------------------
    print("\n\n--- TABELA DE TESTES DO RADIX SORT (Inteiros) ---")
    
    # Cabeçalho da tabela
    print("| Tamanho (N) | Tempo (ms) - Crescente | Tempo (ms) - Decrescente |")
    print("|-------------|------------------------|--------------------------|")
    
    # Linhas de dados
    for i in range(len(tamanhos_de_entrada)):
        tamanho = resultados['Tamanho (N)'][i]
        tempo_cres = resultados['Tempo (ms) - Crescente'][i]
        tempo_decr = resultados['Tempo (ms) - Decrescente'][i]
        
        print(f"| {tamanho:11,} | {tempo_cres:22.4f} | {tempo_decr:24.4f} |")
        
    return resultados

if __name__ == '__main__':
     dados_para_grafico = realizar_teste_de_complexidade_int()