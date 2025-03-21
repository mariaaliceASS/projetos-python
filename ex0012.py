sal = float(input('Insira seu salário: '))
a = sal * 15/100
novosal = sal + a
print('O salário atual de R${:.2f} terá um aumento de R${:.2f}, passando a ser R${:.2f}. '.format(sal, a, novosal))