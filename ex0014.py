km = float(input('Insira quantos Km foram rodados pelo carro: '))
d = float(input('Insira a quantidade de dias em que o carro foi alugado: '))
total = (d*60) + (km*0.15)
print('O custo por {}km rodados e pelo aluguel do veículo por {:.0f} dias é de R${:.2f}'.format(km, d, total))
