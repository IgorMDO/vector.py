# declaração da variável vetor
doisTab = [0,2,4,6,8,10,12,14,16,18,20]

# mostrando os resultados
print(f'2 x 7 = {doisTab[7]}')
print(f'2 x 4 = {doisTab[4]}')

# first and last elements
print(f'first element: {doisTab[0]}')
print(f'last element: {doisTab[-1]}')

# modifying elements
print(f'valor original da posição "{10}" = {doisTab[10]}')
doisTab[10] = 23
print(f'novo valor da posição "{10}" = {doisTab[10]}')

# adding elements
'''
doisTab[11] = 22 # essa forma está incorreta(considerada no Js)
print(f'valor da nova posição {11} = {doisTab[11]}')
'''
doisTab.append(11)
doisTab[11] = 25
print(f'valor de {11} = {doisTab[11]}')
print(f'todos os elementos do vetor: {doisTab}')

# removing elements
doisTab.pop() # obs: o comando "pop" não considerou o elemento adicionado 
print(f'elemento removido: {doisTab.pop()}')
print(f'elementos do vetor: {doisTab}')
#print(f'Último elemento do vetor após remoção: {doisTab[10]}')

# Length
print(f'tamanho do vetor: {len(doisTab)}')
