lista = ["Max", "Dan", "Pippo"]
current_index = 0
while (True):
    print(lista[current_index])
    current_index = current_index + 1
    current_index  = (current_index % 3)
    input("PRESS ENTER")

