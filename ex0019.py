import random

a1 = str(input('Insira o nome do aluno 1: '))
a2 = str(input('Insira o nome do aluno 2: '))
a3 = str(input('Insira o nome do aluno 3: '))
a4 = str(input('Insira o nome do aluno 4: '))
list = [a1,a2,a3,a4]
r = random.choice(list)
print('{} foi escolhido(a) para apagar o quadro.'.format(r))
