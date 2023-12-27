x=1 #int

print("O valor ", x)
print("O tipo: ", type(x)) 

canal="CFB Cursos" #string
s=13.5 #float
r=True #bool
x1=1; x2=2
c=complex(x1,x2)

print(c)

print("O tipo", type(c))

e=["Aula ","de ","Python",1,45.6] #List/Array
e[0]="Curso"
print(e[0],e[1],e[2]) 
print("O tipo", type(e))

e1=("Aula ","de ","Python",1,45.6) #Tupla
print("O tipo", type(e1))

e2={ #dictionary
    "canal":"CFB Cursos",
    "curso":"python",
    "nome":"noejunior299"
}


print("O tipo", type(e2))
print(e2["canal"])

e3={9,8,7,6,5,4,3,2,1,1} #set
e3=frozenset({9,8,7,6,5,4,3,2,1,1})
print("O valor", e3)
print("O tipo", type(e3))