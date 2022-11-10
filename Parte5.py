# Parte 6
# Ciclo While
# esempio
# break, continue, else

i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i+=1

i = 1
while i < 6:
    i+=1
    if i == 3:
        continue # passa alla prossima iterazione
    print(i)
    