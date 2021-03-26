from math import e

an = 0.0000
bn = 0.0000
xn = 0.0000

# MAXIMO DE RESULTADO PARA CALCULAR
max = 9

# PRECISÃO DE CASAS DECIMAIS
prec = 4

def cacl(an,bn,x,cont,anOrbn):
    if (cont == max):
        exit()

    # ENTRE COM A FUNÇÃO AQUI
    # exercico 1 -> func = x**3 - 5*(x**2) + 17*x + 21
    # exercico 2 -> func = e**-x - x
    func = e**-x - x
    if(cont == 0):
        if((an**3 - 5*(an**2) + 17*an + 21) > 0):
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
    cacl(an, bn, x, cont,anOrbn)
    print("-------------------------------------")


if __name__ == '__main__':
    an = float(input("Valor inicial de An: "))
    bn = float(input("Valor inicial de Bn: "))
    x = (an + bn)/2
    cont = 0
    anOrbn = ''
    cacl(an,bn,x,cont,anOrbn)
