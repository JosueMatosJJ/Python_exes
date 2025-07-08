import math
angulo = float(input('Digite o valor do angulo'))
#sin calcula automatico o seno do valor do angulo
seno = math.sin(math.radians(angulo))
#math.cos para cosseno
cosseno = math.cos(math.radians(angulo))
#math.tan para tangente
tangente = math.tan(math.radians(angulo))

print ('O angulo de {}º tem o seno de {:.2f}'
       '\nO angulo de {}º tem o coseno de {:.2f}'
       '\no angulo de {}º tem a tangente de {:.2f}'
       .format(angulo,seno, angulo,cosseno, angulo, tangente))
