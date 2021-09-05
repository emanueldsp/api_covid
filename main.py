import requests

requisicao = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/sp')

rque1 = requisicao.json()

#print(rque1)

print('**-**-- DADOS COVID ESTADO DE SÃO PAULO --**-**')
print('')
print('ULTIMA ATUALIZAÇÃO DE DADOS: '+rque1['datetime'])
print('ESTADO: '+ rque1['state'])
print('NUMERO DE CASOS: ', float(rque1['cases']))
print('NUMERO DE MORTOS: ', float(rque1['deaths']))
print('CASOS SUSPEITOS: ', float(rque1['suspects']))
print('CASOS RECUSADOS: ', float(rque1['refuses']))

print()
input('Tecler enter para sair')