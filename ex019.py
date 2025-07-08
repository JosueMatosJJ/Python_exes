import random
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
nomes = [n1, n2, n3, n4]
#lista com nomes fixos
#nomes = ('Ana', 'Paulo', 'Carlos', 'Bia')
#random.choice escolhe aleatóriamente
print('O nome soretado foi {}'.format(random.choices(nomes)))
