from math import e
import math

an = 0.00000
bn = 0.00000
xn = 0.00000

# condição de parada
parada = 0.01
precParada = 2

# PRECISÃO DE CASAS DECIMAIS
prec = 5

def calc(an,bn,x,cont,anOrbn):
    # ENTRE COM A FUNÇÃO AQUI
    func = x**3 - 2*(x**2) - 20*x + 30
    if(cont == 0):
        if((an**3 - 2*(an**2) - 20*an + 30) > 0):
            anOrbn = 'an'
        else:
            anOrbn = 'bn'
        print(anOrbn)
    anBn = abs(bn - an) / 2
    print("-------------------------------------")
    print("Valor do cont: ", cont)
    print("Valor de An: ", round(an, prec))
    print("Valor de Bn: ", round(bn, prec))
    print("Valor de Xn: ", round(x, prec))
    if(func == 0):
        print("Raiz encontrada ", func)
    elif(func > 0):
        if(anOrbn == 'an'):
            an = x
        else:
            bn = x
    else:
        if (anOrbn == 'an'):
            bn = x
        else:
            an = x
    print("Valor de f(xn): ", round(func, prec))
    x = (an + bn) / 2
    print("Valor ABSOLUTO de (An-Bn)/2: ", round(anBn, prec))
    cont = cont + 1

    stop = round(abs(func), precParada) # Necessario trocar a condição de parada -> ((Bn - An)/2) usar = anBn // para f(Xn) usar = func
    print("STOP", stop)
    print("PARADA", parada)
    if (stop < parada): # Menor, pois assim se for == eu confirmo visualmente se está de acordo.
        exit()


    calc(an, bn, x, cont,anOrbn)
    print("-------------------------------------")


if __name__ == '__main__':
    an = float(input("Valor inicial de An: "))
    bn = float(input("Valor inicial de Bn: "))
    x = (an + bn)/2
    cont = 0
    anOrbn = ''
    calc(an,bn,x,cont,anOrbn)