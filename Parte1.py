# compilare e runnare: python -u nomefile.py

# Parte 2 
# Commenti, Variabili, Tipi di Dati Type(), Input Dati, Casting
# str, int, float, bool, ...  TIPI PRIMITIVI
# list[], tuple(), range(), set{}, dict{k:v}, .... TIPI COMPLESSI


# non e' possibile avere commenti su piu' righe
print ("Hello World")


x = 9
x = 12
y = 3
print(x)
print(type(x))


x = 'ciao'
y = "bellissimo"
print(x + " " + y)

x = False
y = True
print(type(x))

# tipi di dati complessi
x = [1, 2, 3] #lista
y = (1, 2, 3) #tuple
z = range(6) #range
v = {1, 2, 3} #set
g = {"Nome": "Luca", "Cognome": "Rossi", "Eta": 25} #dict 


# input utente
x = input("come ti chiami? ")
print("Ciao " + x)