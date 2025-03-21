import math
co = float(input('Insira o cateto oposto do triângulo retângulo: '))
ca = float(input('Insira o cateto adjacente do triângulo retângulo: '))
h = math.hypot(co,ca)
print("A hipotenusa do triânculo de co {} e ca {} é {:.2f2}".format(co,ca,h))