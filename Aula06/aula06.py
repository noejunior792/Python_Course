curso="Curso de python"

#print(curso[0:5])
print("Tamanho: ", len(curso)) #tamanho da string

print(curso.strip()) #remover espacos

print(curso.lower())
print(curso.upper())
print(curso.replace("python","C#").replace("Curso","Academia"))
a=curso.split(" ")
print(a[0:3])