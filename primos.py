def primes_recursive(n):
    #Valida o input
    if (n < 2):
        return False

    #Casos específicos que a lógica da função não cobre
    if (n == 2):
        return [2]
    if (n == 3):
        return [2, 3]

    #Caso o input seja par, permite fazer a recursão com n - 2 na linha 21 e acredito que isso deixa a função um pouco mais rápida
    if (n % 2 == 0):
        return primes_recursive(n-1)

    #Como nenhum número que termina com 5 é primo (tirando o próprio 5), ele é pulado. Acredito que deixa a função um pouco mais rápida
    if (n != 5 and n % 5 == 0):
        return primes_recursive(n-2)

    #Recursividade
    resposta = primes_recursive(n-2)

    #Verifica se N é divisível por números primos menores que ele
    raiz = int(n**(1/2) + 1)
    for i in resposta:
        #N é divisível, então não é incluído na resposta
        if (n % i == 0):
            return resposta

        #Um número não é divisível por outro número maior que sua raiz
        if (i > raiz):
            break

    # N não é divisível, então é incluído na resposta
    resposta.append(n)
    return resposta

def primes_iterative(n):
    #Valida o input
    if (n < 2):
        return False

    resposta = [2]

    #Casos específicos que a lógica da função não cobre
    if (n == 2):
        return resposta

    #Iterações
    for i in range(3, n+1, 2):

        max = int(i**(1/2) + 1) #Um número não é divisível por outro que seja maior que sua raíz
        teste = True #Hipótese de que o número i é primo

        #Divide i por todos os números menores que sua raíz
        for o in range(3, max, 2):
            if (i % o == 0):
                teste = False #i é divisível
                break

        #Se i for primo, adiciona ele na lista de números primos
        if teste:
            resposta.append(i)

    return resposta

if __name__ == "__main__":
    n = int(input("Valor de N: "))

    print("Função recursiva: ", primes_recursive(n))
    print("Função iterativa: ", primes_iterative(n))


