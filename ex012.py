
print ('Quero desconto!!')
preco = float(input('OK senhor qual é o valor do produto desejado?'))
pixdin = float (preco*0.9)
debito = float(preco*0.95)
print ('O valor do produto escolhido é {}'.format(preco))
pay = input ('Qual a forma de pagamento?')
if pay == 'pix' or pay == 'dinheiro':
        print ('Vai ficar {:.2f} Reais '.format(pixdin))
elif pay == 'debito':
        print ('Vai ficar {:.2f} Reais '.format(debito))
elif pay == 'credito':
    credit = float(input ('Em quantas vezes? Pode parcelar até 12!'))
    print ('Vai ficar {} X de {:.2f} sem juros'.format(credit,preco/credit))