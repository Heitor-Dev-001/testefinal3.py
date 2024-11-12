#Qual das opções a seguir é a única que NÃO É um tipo primitivo em Python?

opcoes = ['double', 'float', 'int', 'bool'] # Lista crida
print('-=-' * 20)

#Pergunta ao usuário
print('Dos resultados acima, qual é sua resposta?:{}'.format(opcoes))

#Entrada do usuário
print('-=-' * 20)
resposta = input('Escolha uma opção:')


#Verifica a resposta e exibe a mensagem correta
if resposta == 'float':
    print('float é um valor primitivo em Python')
elif resposta == 'int':
    print('int é um valor primitivo em python')
elif resposta =='bool':
    print('bool é um valor primitivo em Python')
else:
    print('double não é um valor primitivo em python')




