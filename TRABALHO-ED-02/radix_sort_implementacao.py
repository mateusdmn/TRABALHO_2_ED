import time
import random

# =================================================================
# FUNÇÕES DE ORDENAÇÃO DE INTEIROS (RADIX SORT NUMÉRICO)
# =================================================================

def counting_sort_int(lista, exponencial, base=10):
    """Ordena a lista de inteiros com base no dígito de uma posição específica."""
    n = len(lista)
    resultado = [0] * n
    contagem = [0] * base 

    for i in range(n):
        # Isola o dígito (unidade, dezena, etc.)
        indice_digito = (lista[i] // exponencial) % base
        contagem[indice_digito] += 1

    for i in range(1, base):
        contagem[i] += contagem[i - 1]

    i = n - 1
    while i >= 0:
        indice_digito = (lista[i] // exponencial) % base
        posicao = contagem[indice_digito] - 1
        resultado[posicao] = lista[i]
        contagem[indice_digito] -= 1
        i -= 1

    for i in range(n):
        lista[i] = resultado[i]

def radix_sort_int(lista, crescente=True):
    """Ordena uma lista de números inteiros positivos usando o Radix Sort."""
    if not lista:
        return []
        
    maior_numero = max(lista)
    
    exp = 1
    while maior_numero // exp > 0:
        counting_sort_int(lista, exp, base=10)
        exp *= 10
        
    # Lógica para ordenamento Decrescente
    if not crescente:
        lista.reverse()
        
    return lista

# =================================================================
# FUNÇÕES DE ORDENAÇÃO DE STRINGS (RADIX SORT PARA DEMONSTRAÇÃO)
# =================================================================

def counting_sort_strings(lista, indice_caractere, alfabeto_tamanho=256):
    """Ordena a lista de strings com base no caractere na posição 'indice_caractere'."""
    n = len(lista)
    resultado = ["" for _ in range(n)] 
    contagem = [0] * alfabeto_tamanho 
    
    for s in lista:
        char_code = ord(s[indice_caractere]) if indice_caractere < len(s) else 0
        contagem[char_code] += 1

    for i in range(1, alfabeto_tamanho):
        contagem[i] += contagem[i - 1]

    i = n - 1
    while i >= 0:
        s = lista[i]
        char_code = ord(s[indice_caractere]) if indice_caractere < len(s) else 0
        
        posicao = contagem[char_code] - 1
        resultado[posicao] = s
        
        contagem[char_code] -= 1
        i -= 1

    for i in range(n):
        lista[i] = resultado[i]

def radix_sort_strings(lista):
    """Ordena uma lista de strings usando o LSD Radix Sort (somente crescente)."""
    if not lista:
        return []

    max_len = max(len(s) for s in lista)

    # Iterar do menos significativo (fim) ao mais significativo (início)
    for i in range(max_len - 1, -1, -1):
        counting_sort_strings(lista, i)
        
    return lista

# =================================================================
# EXEMPLOS DE USO (SAÍDAS NECESSÁRIAS PARA O TÓPICO 2.1)
# =================================================================

if __name__ == '__main__':
    
    # 1. SAÍDA DE NÚMEROS (Inteiros)
    dados_numeros = [170, 45, 75, 90, 802, 24, 2, 66]
    
    # Crescente
    lista_crescente = dados_numeros.copy()
    radix_sort_int(lista_crescente, crescente=True)
    print("--- Saída de Números (Inteiros) ---")
    print(f"Lista Crescente: {lista_crescente}") 
    
    # Decrescente
    lista_decrescente = dados_numeros.copy()
    radix_sort_int(lista_decrescente, crescente=False)
    print(f"Lista Decrescente: {lista_decrescente}")

    # 2. SAÍDA DE STRINGS (Strings)
    dados_strings = ["banana", "uva", "abacaxi", "laranja", "peraa"]
    strings_ordenadas = dados_strings.copy()
    radix_sort_strings(strings_ordenadas) # Radix Sort de strings ordena lexicograficamente (crescente)
    print("\n--- Saída de Strings ---")
    print(f"Strings Ordenadas: {strings_ordenadas}")