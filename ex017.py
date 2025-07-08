import math
catop = float(input('Digite o valor do cateto oposto:'))
catad = float(input('Digite o valor do cateto adjacente:'))
#hypot calcula o valor automatico das somas do cateto ao ²
hip = math.hypot(catop, catad)
print ('A hipotenusa vale {}'.format(hip))
