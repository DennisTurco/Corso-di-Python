# Parte 13
# funzioni
# creare, chiamare, parametri, default, return

def saluta():
    print("ciao")

def saluta(nome):
    print("ciao sono " + nome)

def saluta2(nome = "Luca"): # posso aggiungere parametri di default
    print("ciao sono " + nome)

def calcolo(x, y):
    somma = x + y
    return somma


saluta("Marco") #chiamata di funzione

risultato = calcolo(2, 3)
print(risultato)