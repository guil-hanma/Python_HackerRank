if __name__ == '__main__':
    print("Este programa pega um numero X e printa ele a mesma quantidade de vezes que ele mesmo, multiplicando cada numero por sí mesmo até chegar no numero X")
    n = int(input("Escreva qual número você quer loopar: "))
    for i in range(n):
        print(i*i)
