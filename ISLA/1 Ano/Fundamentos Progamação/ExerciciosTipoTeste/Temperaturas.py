"""
Faça um algoritmo em Python que leia um conjunto de 20 temperaturas em graus 
celsius (pode ter casas decimais). O algoritmo deve apresentar no ecrã a média
das temperaturas, a temperatura máxima e temperatura mínima.
"""
temperaturas = []
media = 0
tam_lista = 5

for i in range(tam_lista):
    temperatura = float(input(f"Digite a {i+1}º temperatura em graus Celsius: "))
    media = media + temperatura/tam_lista
    temperaturas.append(temperatura)

media = sum(temperaturas)/len(temperaturas)
print("Media: ", media)
print("Maximo: ", max(temperaturas))
print("Minimo: ", min(temperaturas))


print("Temperaturas: ", temperaturas)