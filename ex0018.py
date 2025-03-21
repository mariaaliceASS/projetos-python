import math
a = float(input('Insira um ângulo: '))
s = math.sin(math.radians(a))
print('O seno do ângulo {}º é {:.2f}.'.format(a,s))
c = math.cos(math.radians(a))
print('O cosseno do ângulo {}º é {:.2f}.'.format(a,c))
t = math.tan(math.radians(a))
print('A tangente do ângulo {}º é {:.2f}.'.format(a,t))
