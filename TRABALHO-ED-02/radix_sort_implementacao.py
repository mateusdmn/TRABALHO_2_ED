import time
import random

# =================================================================
# FUNÇÕES DE ORDENAÇÃO DE INTEIROS (RADIX SORT NUMÉRICO)
# Este bloco implementa o Counting Sort e o Radix Sort para números inteiros,
# que é a base para a avaliação de desempenho (Tópicos 2.2 e 2.3).
# =================================================================

def counting_sort_int(lista, exponencial, base=10):
    """
    Função auxiliar que ordena a 'lista' com base no dígito especificado pela 'exponencial'.
    O Radix Sort chama esta função d vezes (onde d é o número de dígitos).
    """
    n = len(lista)
    resultado = [0] * n  # Array de saída para armazenar a lista ordenada na passagem atual
    contagem = [0] * base  # Array de contagem (tamanho 10 para base decimal)

    # 1. Contar a frequência de cada dígito na posição atual (exponencial)
    for i in range(n):
        # Isola o dígito (unidade, dezena, etc.)
        indice_digito = (lista[i] // exponencial) % base
        contagem[indice_digito] += 1

    # 2. Modificar o array de contagem para conter a posição real dos elementos
    # Isso garante que o algoritmo seja estável, preservando a ordem dos elementos com o mesmo dígito.
    for i in range(1, base):
        contagem[i] += contagem[i - 1]

    # 3. Construir o array de saída (resultado)
    i = n - 1
    while i >= 0:
        # Encontra o dígito na posição atual
        indice_digito = (lista[i] // exponencial) % base
        
        # Encontra a posição correta no array de saída
        posicao = contagem[indice_digito] - 1
        resultado[posicao] = lista[i]
        
        # Decrementa a contagem para o próximo número com o mesmo dígito
        contagem[indice_digito] -= 1
        i -= 1

    # 4. Copiar os elementos ordenados de volta para a lista original
    for i in range(n):
        lista[i] = resultado[i]

def radix_sort_int(lista, crescente=True):
    """
    Função principal que implementa o Radix Sort.
    Determina o número de dígitos (d) e chama o Counting Sort para cada dígito.
    """
    if not lista:
        return []
        
    # 1. Encontrar o maior número para saber quantas vezes o Counting Sort deve ser executado
    maior_numero = max(lista)
    
    # 2. Iterar sobre os dígitos, da direita para a esquerda (LSD - Least Significant Digit)
    exp = 1 # O expoente começa em 1 (unidades), depois 10 (dezenas), 100 (centenas), etc.
    while maior_numero // exp > 0:
        counting_sort_int(lista, exp, base=10)
        exp *= 10
        
    # 3. Lógica para ordenamento Decrescente (Requisito 2.1)
    # Se a flag crescente for False, a lista é revertida.
    if not crescente:
        lista.reverse()
        
    return lista

# =================================================================
# FUNÇÕES DE ORDENAÇÃO DE STRINGS (RADIX SORT PARA DEMONSTRAÇÃO)
# Este bloco demonstra a capacidade do algoritmo de lidar com outros tipos de dados (Requisito 2.2).
# =================================================================

def counting_sort_strings(lista, indice_caractere, alfabeto_tamanho=256):
    """
    Função auxiliar adaptada para ordenar strings com base no caractere na 'indice_caractere'.
    Utiliza o valor ASCII (0-255) como "dígito".
    """
    n = len(lista)
    resultado = ["" for _ in range(n)] 
    contagem = [0] * alfabeto_tamanho 
    
    # 1. Contar a frequência de cada caractere na posição atual
    for s in lista:
        # Usa o código ASCII (ord()) como índice. Se a string for curta, usa 0 (padding).
        char_code = ord(s[indice_caractere]) if indice_caractere < len(s) else 0
        contagem[char_code] += 1

    # 2. Modificar o array de contagem para posições reais (garantindo estabilidade)
    for i in range(1, alfabeto_tamanho):
        contagem[i] += contagem[i - 1]

    # 3. Construir o array de saída (iterando de trás para frente)
    i = n - 1
    while i >= 0:
        s = lista[i]
        char_code = ord(s[indice_caractere]) if indice_caractere < len(s) else 0
        
        posicao = contagem[char_code] - 1
        resultado[posicao] = s
        
        contagem[char_code] -= 1
        i -= 1

    # 4. Copiar os elementos ordenados de volta
    for i in range(n):
        lista[i] = resultado[i]

def radix_sort_strings(lista):
    """
    Função principal do Radix Sort adaptada para strings.
    Itera sobre o tamanho máximo das strings, do último caractere ao primeiro.
    """
    if not lista:
        return []

    # Encontrar o comprimento da string mais longa (max_len)
    max_len = max(len(s) for s in lista)

    # Iterar do menos significativo (fim) ao mais significativo (início). 
    # Para strings, isso garante a ordem lexicográfica.
    for i in range(max_len - 1, -1, -1):
        counting_sort_strings(lista, i)
        
    return lista

# =================================================================
# EXEMPLOS DE USO (SAÍDAS NECESSÁRIAS PARA O TÓPICO 2.1)
# Este bloco de código demonstra a correção e o funcionamento do algoritmo.
# =================================================================

if __name__ == '__main__':
    
    # 1. SAÍDA DE NÚMEROS (Inteiros) - Demonstração dos Requisitos Crescente/Decrescente
    dados_numeros = [170, 45, 75, 90, 802, 24, 2, 66]
    
    # Crescente (Requisito de Ordenamento)
    lista_crescente = dados_numeros.copy()
    radix_sort_int(lista_crescente, crescente=True)
    print("--- Saída de Números (Inteiros) ---")
    print(f"Lista Crescente: {lista_crescente}") 
    
    # Decrescente (Requisito de Ordenamento)
    lista_decrescente = dados_numeros.copy()
    radix_sort_int(lista_decrescente, crescente=False)
    print(f"Lista Decrescente: {lista_decrescente}")

    # 2. SAÍDA DE STRINGS (Strings) - Demonstração de Variedade de Tipos de Dados (Requisito 2.2)
    dados_strings = ["banana", "uva", "abacaxi", "laranja", "peraa"]
    strings_ordenadas = dados_strings.copy()
    # O Radix Sort de strings ordena lexicograficamente (crescente)
    radix_sort_strings(strings_ordenadas) 
    print("\n--- Saída de Strings ---")
    print(f"Strings Ordenadas: {strings_ordenadas}")
