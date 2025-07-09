print('Quero desconto!!')
preco = float(input('OK senhor, qual é o valor do produto desejado? R$ '))
pixdin = preco * 0.9
debito = preco * 0.95

print('\nO valor do produto escolhido é: R$ {:.2f}'.format(preco))
#strip remove os espços no inicio e no final do inserido pelo usuario
#lower deixa tudo em letra minuscula
pay = input('Qual a forma de pagamento? (pix, dinheiro, debito ou credito): ').strip().lower()
#if condicional SE
if pay in ['pix', 'dinheiro']:
    print('Com desconto, vai ficar: R$ {:.2f}'.format(pixdin))
# se a condicional anterior nao for verdadeira esta será executada
elif pay == 'debito':
    print('Com desconto, vai ficar: R$ {:.2f}'.format(debito))

elif pay == 'credito':
    credit = int(input('Em quantas vezes? Pode parcelar até 12: '))
    if 1 <= credit <= 12:
        parcela = preco / credit
        print('Vai ficar {}x de R$ {:.2f} sem juros'.format(credit, parcela))
    else:
        print('Número de parcelas inválido. Deve ser entre 1 e 12.')
 #se senhuma das condiçoes anteriores forem atendidas           
else:
    print('Forma de pagamento não reconhecida.')
