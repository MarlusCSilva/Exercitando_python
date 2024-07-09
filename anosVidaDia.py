"""
Algoritomo para ler o nome e idade de uma pessoa e exibir os anos em dias. 

"""

nome=input("Digite o nome do abençoado: ")
idade=int(input("Digite a idade do abençoado: "))

dias = 365 * idade

print(f"O(a) {nome} tem {idade} anos e possui {dias} em dias")