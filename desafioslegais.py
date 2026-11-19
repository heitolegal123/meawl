

#1.Faça um programa que recebe um número de 1 a 10 e imprime a tabuada desse número.
#2.Faça um programa que recebe do usuário 10 valores de números inteiros, armazena em um vetor e após percorrê-lo exibe qual é o maior valor e a sua posição.

#1
'''num = int(input(">>>"))


for a in range(1,11):
    mult = num * a
    print(mult)
'''

#2



lista = list()
for a in range (1,11):
    print(a)
    lista.append  (int(input("digite dez numeros: ")))

def verificador_de_maior(lista) :
    maior = lista[0]
    for a in lista:
        if a > maior:
            maior = a
    return maior
    

















































































