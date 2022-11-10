# Parte 8
# list
# introduzione, creazione, lettura, modifica
# range di elementi
# inserire elementi insert() append()
# rimuovere con remove() pop() clear()
# le liste sono ordinate, modificabili e permettono duplicati e vanno da 0 a n

citta = ["Milano", "Torino", "Bologna", "Bologna"]
citta[3] = "Venezia"
print(citta)
print(citta[0:2])

citta.insert(0, "Roma")
print(citta)

citta.append("LaSpezia")
print(citta)

citta.pop() # rimuove l'ultimo elemento
print(citta)

citta.pop(0)
print(citta)

citta = ["Milano", "Torino", "Bologna"]
print(citta[-1]) #posso ottenere gli elementi anche tramite valori negativi

print(len(citta))