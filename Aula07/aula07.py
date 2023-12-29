texto="Curso de Python"
palavra="python"

res=palavra.upper() in texto.upper()
print(res)
"""res="Python" not in texto
print(res)

res="Python" in texto
print(res)"""

dia=15
mes="Dezembro"
ano=2023
cidade="Luanda"
data="{}, {} de {} de {}"
print(data.format(cidade,dia,mes,ano))

#\' \"" \n \r \t \b