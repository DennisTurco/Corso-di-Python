# Parte 12
# Dictionaries (simili alle struct di c++)
# introduzione
    # ordinati (da python 3.7), modificabili, no duplicati
# accesso get(), keys(), values(), items()
# if key in dict
# inserisci/modifica con [] o update()
# pop(), clear(), loop(), nested

persona = {
    "nome": "Luca",  #"nome" = chiave, "Luca" = valore
    "cognome": "Rossi",
    "eta": 25
}

print(persona.get("nome"))

print()

print(persona.keys())

print()

print(persona.values())

print()

print(persona.items())


if "nome" in persona:
    print("ok")


print()

# inserimento
persona['scuola'] = "Istituto Superiore"
print(persona)


# modifica
persona['nome'] = "Marco"
print(persona)


# modifica/aggiunta
persona.update({"nome":"Dennis"})
print(persona)

# modifica/aggiunta
persona.update({"sesso":"Maschio"})
print(persona)


#eliminare elemento in coda
persona.popitem()
print(persona)


for i in persona:
    print(i)

print()

# pulire
persona.clear()
print(persona)



persona = {
    "nome": "Luca",  #"nome" = chiave, "Luca" = valore
    "cognome": "Rossi",
    "eta": 25,
    "indirizzo": {
        "nazione": "Italia",
        "regione": "Lombardia",
        "citta": "Padova"
    }
}

print(persona["indirizzo"]["nazione"])