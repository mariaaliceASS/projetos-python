price = float(input('Insira o valor do produto: '))
nprice =  price - (price * 0.05)
print('O novo valor do produto com 5% de desconto é de R${:.2f}'.format(nprice))