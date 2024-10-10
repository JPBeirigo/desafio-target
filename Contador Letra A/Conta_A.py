def conta_letra_a(texto):
    # Converte o texto para minúsculo para contar 'a' e 'A' juntos
    texto_minusculo = texto.lower()
    
    # Conta o número de ocorrências da letra 'a'
    quantidade = texto_minusculo.count('a')
    
    # Encontra as posições de todas as letras 'a' (maiúsculas e minúscualas)
    posicoes = [i for i, letra in enumerate(texto) if letra.lower() == 'a']
    
    return quantidade, posicoes

def main():
    # Solicita a entrada do usuário
    texto = input("Digite um texto: ")
    
    # Verifica se o texto está vazio
    if not texto:
        print("O texto está vazio!")
        return
    
    # Obtém a quantidade e posições das letras 'a'
    quantidade, posicoes = conta_letra_a(texto)
    
    # Exibe os resultados
    if quantidade > 0:
        print(f"\nA letra 'a' aparece {quantidade} vez(es) no texto.")
        print("Posições:", end=" ")
        for i, pos in enumerate(posicoes):
            letra_original = texto[pos]
            print(f"{pos}({letra_original})", end="")
            if i < len(posicoes) - 1:
                print(", ", end="")
        print()  # Nova linha após listar todas as posições
    else:
        print("A letra 'a' não aparece no texto.")
    
    # Mostra o texto original para referência
    print(f"\nTexto original: {texto}")

if __name__ == "__main__":
    main()