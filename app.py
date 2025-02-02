import re
from collections import Counter


def ler_texto_arquivo(caminho_arquivo):
    """Lê o conteúdo de um arquivo e retorna como uma string."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print("Arquivo não encontrado. Por favor, verifique o caminho e tente novamente.")
        return None

def contar_palavras(texto):
    """Conta o número de palavras no texto."""
    palavras = texto.split()
    return len(palavras)

def contar_frases(texto):
    """Conta o número de frases no texto."""
    # frases terminadas por '.', '!', ou '?'
    frases = re.split(r'[.!?]+', texto)
    return len([frase for frase in frases if frase.strip()])

def frequencia_palavras(texto):
    """Calcula a frequência de cada palavra no texto."""
    palavras = re.findall(r'\b\w+\b', texto.lower())  # Encontra todas as palavras
    return Counter(palavras)

def palavra_mais_frequente(frequencias):
    """Encontra a palavra mais frequente e sua contagem."""
    if frequencias:
        return frequencias.most_common(1)[0]  # Retorna a palavra mais comum e sua contagem
    return "", 0

def contar_caracteres(texto):
    """Conta diferentes tipos de caracteres no texto."""
    letras = sum(c.isalpha() for c in texto)
    numeros = sum(c.isdigit() for c in texto)
    pontuacao = sum(not c.isalnum() and not c.isspace() for c in texto)
    
    return {
        'Letras': letras,
        'Números': numeros,
        'Pontuação': pontuacao,
        'Total': len(texto)
    }

def main():
    print("Bem-vindo ao analisador de texto!")
    
    escolha = input("Você deseja (1) digitar um texto ou (2) ler de um arquivo? (Digite 1 ou 2): ")
    
    if escolha == '1':
        texto = input("Digite seu texto: ")
    elif escolha == '2':
        caminho_arquivo = input("Digite o caminho do arquivo: ")
        texto = ler_texto_arquivo(caminho_arquivo)
        if texto is None:
            return  # Se não ler o arquivo, encerra a função
    else:
        print("Escolha inválida. Encerrando o programa.")
        return
    
    print("\nAnálise do Texto:")
    
    num_palavras = contar_palavras(texto)
    num_frases = contar_frases(texto)
    
    frequencias = frequencia_palavras(texto)
    
    palavra_frequente, contagem_frequente = palavra_mais_frequente(frequencias)
    
    contagem_caracteres = contar_caracteres(texto)

    print(f"Número de palavras: {num_palavras}")
    print(f"Número de frases: {num_frases}")
    
    print("\nFrequência das palavras:")
    for palavra, contagem in frequencias.items():
        print(f"{palavra}: {contagem}")
    
    print(f"\nA palavra mais frequente é: '{palavra_frequente}' com {contagem_frequente} ocorrências.")
    
    print("\nContagem de diferentes tipos de caracteres:")
    for tipo, contagem in contagem_caracteres.items():
        print(f"{tipo}: {contagem}")

if __name__ == "__main__":
    main()


