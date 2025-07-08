#arredondamento matematico automatico para cima ou para baixo
num1 = float (input('Digite um valor Real:'))
print ('O valor arredondado é {:.0f}'.format(num1))

import math
num2 = float(input('Digite um valor Real para arredondar para baixo'))
num3 = math.floor(num2)
print ('o valor inteiro é {}'.format(num3))
