carros=["HRV","Golf","Argo","Focus"]
carros[3]="Fusion"
print(carros)
print(carros[-1])

carros.append("Fit")
carros.append("Fusion")
carros.append("Polo")

print(len(carros), " carros na lista")

carros.remove("Fusion")

print(len(carros), " carros na lista")

print(carros)

carros.pop() #elimina o ultimo item da lista

print(carros)

#del carros[3] #limpa o index
#carros.clear() limpa toda lista

carros2=list(carros)
print("Carros2: ",carros2)

carros2=["Luanda","Angola","Africa"]
carros3=carros+carros2
print(carros3) 