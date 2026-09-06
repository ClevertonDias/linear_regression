#Programa Regressão linear


import matplotlib.pyplot as plt

valida = False


####################Qual o número de pontos medidos?##############################
while valida == False:                                                           #
                                                                                 #
	v = input('Digite a quantidade de pontos que você deseja inserir: ')     #
	try:                                                                     #
		v = int(v)                                                       #
		if v > 0:                                                        #
			valida = True                                            #
		else:                                                            #
			print('Por favor!, digite um inteiro maior que zero.')   #
	except:                                                                  #
		print('Por favor!, digite um inteiro maior que zero.')           #
##################################################################################
print('\n')

##Pontos experimentais, inserindo os pontos:

cont = 1 # contador
valida = False

#Listas dos pares ordenados:
lista_x = []
lista_y = []



# inserindo os pontos (x, y):
while cont <= v:
	print('\n')
	print('Inserindo o ponto', str(cont))
	

	while valida == False:
		g = input('digite o valor de x: ')

		try:
			g = float(g)
			if g >= 0 or g < 0:
				lista_x.append(g)
				valida = True
		except:
			print('Digite um valor válido')

	valida = False


	while valida == False:
		g = input('digite o valor de y: ')
		
		try:
			g = float(g)
			if g >= 0 or g < 0:
				lista_y.append(g)
				valida = True
		except:
			print('Digite um valor válido')



	print('ponto', str(cont), 'foi inserido')
	valida = False
	cont = cont + 1 

print('Você inseriu', str(v), 'pontos')
#########################################################################

#Encontrado os coeficientes da reta:

cont1 = 0 
cont2 = 0

for i in range(0, v, 1):
	cont1 = cont1 + (lista_x[i]*lista_y[i])
	cont2 = cont2 + (lista_x[i]**2)

a = ((v*cont1)-(sum(lista_x)*sum(lista_y)))/((v*cont2)-((sum(lista_x))**2)) # coeficiente angular da reta	

b = (sum(lista_y)-(a*(sum(lista_x))))/v # coeficiente angular da reta

lista_regression = [] #lista para inserir f(x) = ax + b

for i in lista_x:
	lista_regression.append(a*i + b)

print('coeficiente angular: ', round(a,3))
print('coeficiente linear: ', round(b,3))

print('\n')

#PLotando os gráficos:

plt.plot(lista_x, lista_y, 'o')
plt.plot(lista_x, lista_regression)
plt.show()



