fi = open("dataset_revision_clean.txt", "r")
array = [0, 0, 0, 0, 0]
err = 0
total = 0
over_35 = 0
over_30 = 0
maximo = 5
minimo = 9999
suma = 0
for i in fi:
	variable = i.strip()
	#variable = variable.replace(".", ",")
	variable = variable.split(" ")
	print(variable)
	if(variable[1] != "err"):
		if (float(variable[1]) < 1):
			array[0] = array[0] + 1
		elif (float(variable[1]) < 2):
			array[1] = array[1] + 1
		elif (float(variable[1]) < 3):
			array[2] = array[2] + 1
		elif (float(variable[1]) < 4):
			array[3] = array[3] + 1
		elif (float(variable[1]) < 5):
			array[4] = array[4] + 1
		if (float(variable[1]) < minimo):
			minimo = float(variable[1])
		if (float(variable[1]) >= 3):
			over_30 = over_30 + 1
		if (float(variable[1]) >= 3.5):
			over_35 = over_35 + 1
		total = total + 1
		suma = suma + float(variable[1])
	else:
		err = err + 1
print(array)
print(err)
print("\n\n")
print("Posibles Bots: " + str(total + err))
print("Cuentas Estudiadas:" + str(total))
#print("Cuentas con un Valor superior a 3: " + str(over_30 + err))
#print("Cuentas con un Valor superior a 3.5: " + str(over_35 + err))
#print("Efectividad (3) : " + str((over_30 + err)/total*100) + "%")
#print("Efectividad (3.5) : " + str((over_35 + err)/total*100) + "%")
print("Cuentas con un Valor superior a 3: " + str(over_30))
print("Cuentas con un Valor superior a 3.5: " + str(over_35))
print("Efectividad (3) : " + str((over_30)/total*100) + "%")
print("Efectividad (3.5) : " + str((over_35)/total*100) + "%")
print("Media: " + str((suma/total)))
print("Media2: "+ str(((suma + 5*err)/total)))
print("\n")
print("Distribuciones:\n")
print("Valor [0,1[: " + str(array[0]))
print("Valor [1,2[: " + str(array[1]))
print("Valor [2,3[: " + str(array[2]))
print("Valor [3,4[: " + str(array[3]))
print("Valor [4,5]: " + str(array[4]))
print("\n")
print("Valor Maximo Botometro: " + str(maximo))
print("Valor minimo Botometro: " + str(minimo))

