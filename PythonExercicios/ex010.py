real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.33
euro = real / 5.30
print('Com R${:.2f} você pode comprar US${:.2f} em Dolares ou €${:.2f} em Euros'.format(real, dolar, euro))
