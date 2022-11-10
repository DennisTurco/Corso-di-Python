# Parte 10
# Tuple (lista costante di elementi)
# introduzione
# ordinate, immutabili con duplicati
# creare, accedere, modifica?, spaccettare
# loop
# count() index()

citta = ("Milano", "Torino", "Bologna") #tupla
print(citta)
print(citta[0])
# citta[0] = "Roma" non si puo' fare perche' non modificabili

# per modificare occorre:
x = list(citta)
x.append("Roma")
citta = tuple(x)
print(citta)

# spacchettamento
citta = ("Milano", "Torino", "Bologna")
(x, y, z) = citta
print(x)
print(y)
print(z)


citta = ("Milano", "Torino", "Bologna", "Bologna")
print(citta.count("Bologna"))
print(citta.count("Torino"))
print(citta.index("Milano"))