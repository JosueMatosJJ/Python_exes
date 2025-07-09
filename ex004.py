a = input('Digite algo')
print('O tipo primitivo dessa classe é', type(a))      # Exibe o tipo da variável (sempre 'str' ao usar input)
print('Só tem espaço?', a.isspace())                    # Verifica se a string contém apenas espaços
print('É um número?', a.isnumeric())                    # Verifica se a string contém apenas dígitos numéricos
