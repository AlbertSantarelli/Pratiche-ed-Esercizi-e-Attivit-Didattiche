#Programma Ricercatore by Albert Santarelli
import time

#colors
Verde = "\033[92m"
Rosso = "\033[91m"
Normale = "\033[0m"
Giallo = "\033[93m"

#Crea una Variabile con il tuo nome e stampala.
Nome = "AlbertSantarelli"
print(Nome)
Noome = input("Come ti chiami ?  ")

#Criedi all'utente la sua eta e stampala raddopiata.
Eta = int(input("Quanti Anni Hai ?  "))

if Eta < 10:
    print("Non Dovresti Dire Bugie")
else:
    print(Eta * 2, "Sei Molto Vecchio")

#Crea due numeri e stampa la loro somma.
Regole = ("Facciamo un gioco. Io indovino la somma di due numeri che scegli !")
print(Regole)
X = int(input("Inserisci un numero casuale.  "))
Y = int(input("Inserisci altro numero casuale.  "))

print (f"{Rosso}Procedendo nel complesso...{Normale}")
time.sleep(5)

print(f"{Giallo}Hacking del satellite della Nasa...{Normale}")
time.sleep(5)

print(f"{Verde}Sistema hackerato con successo.{Normale}")
time.sleep(5)

print("Hai",Eta,"Anni","Ti chiami",Noome,"La somma dei due numeri e",X+Y)