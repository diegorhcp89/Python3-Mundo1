nome = 'Diego'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\33[7:30m'
         }
print('Olá! Muito prazer em te conheceer, {}{}{}' .format(cores['azul'], nome, cores['limpa']))
