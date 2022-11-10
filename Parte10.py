# Parte 11
# Set
# introduzione
    # non ordinati, non indexati, non modificabili, no duplicati
# accesso con loop
# add() update() remove() vs discard() clear()

citta = {"Milano", "Torino", "Bologna"}
# citta[1] = "Torino" --> errore


citta = {"Milano", "Torino", "Bologna", "Bologna"}
print(citta) # "bologna" lo stamperà una sola volta (no duplicati)


citta.add("Roma")
print(citta)
citta.clear() # per pulire


citta = {"Milano", "Torino", "Bologna"}
altre_citta = {"Napoli", "Venezia"}
citta.update(altre_citta)
print(citta)


# la differenza tra remove e discad è che se provo una remove su 
# un elemento che non c'è mi da errore, con discard no


citta = {"Milano", "Torino", "Bologna"}
for x in citta:
    print(x)


# Nota: l'ordine in cui stampa il Set non ha un ordine preciso, provare a stampare
# diverse volte