print ('Bem vindo a Alucar !')
dia = int (input('Quantos dias o Sr(a) permaneceu com o carro?'))
km = float(input ('Qual foi a kilometragem percorrida nesses dias?'))
total = (dia * 60) + (km * 0.15)
print ('Obrigado por usar a Alucar \nO seu valor total é '
       'de R${:.2f}\nVolte sempre!'.format(total))