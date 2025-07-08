alt = float(input('Qual a altura da parede em metros?'))
larg = float(input('Qual é a largura da parede em metros?'))
area = float (alt * larg)
tinta = float( area /2)
print('Serão necessários {:.2f} litros de tinta para pintar '
      '{:.2f} metros da parede.'.format(tinta, area))