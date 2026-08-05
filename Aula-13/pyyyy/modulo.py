import random


def atv_1():
    n = random.randint(5,10)
    return n



def atv_2():
    n1 = random.randint(5,10)
    n2 = random.randint(5,10)
    n3 = random.randint(5,10)
    return n1,n2,n3
    

def atv_3():
    n = random.randint(10,30)
    return n

def atv_4():
    for contagem in range(10,0,-1):
        print(contagem)
    print('fogo!')    

def atv_6():
    numero = int(input("digite um numero de 0 a 10"))

    soma = 0

    for i in range(2, numero + 1):
       if i %2==0:
           soma += i

           print("A soma dos numeros pares é: ", soma)
