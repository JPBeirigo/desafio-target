def is_fibonacci(numero):
    if numero < 0:
        return False
    
    anterior, atual = 0, 1
    
    while atual < numero:
        anterior, atual = atual, anterior + atual
    
    return atual == numero or numero == 0

def main():
    try:
        numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
        
        if is_fibonacci(numero):
            print(f"{numero} faz parte da sequência de Fibonacci!")
        else:
            print(f"{numero} não faz parte da sequência de Fibonacci.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()