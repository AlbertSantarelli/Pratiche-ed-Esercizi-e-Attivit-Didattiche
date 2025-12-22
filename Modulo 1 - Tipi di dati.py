#Programma by Albert Santarelli
#Crea una variabile x con valore 7 e una y con valore 3. Stampa la somma dei due numeri.
 
Inizio = "Rinforzo della lezione di matematica"   #GlobalScoope

X = 7
Y = 3

Soma = (X + Y)

Problema = print ("Se ho ",X, "case", "e ne ho comprati altri", Y, "case") 
Domanda = int(input("Qual è il risultato della somma dei due valori ? "))

if Domanda == 10:
    print("Perfetto, complimenti, il risultato è",Soma,"Supererai l'anno scolastico...")  #LocalScoope
else:
    print("Riprova la prossima volta, studia di piu")

#Crea una variabile prezzo con valore 19.99 e una quantità con valore 3. Stampa il totale (prezzo × quantità).

Inizio1 = "Controllo dell'inventario e fatturazione futura !" #GlobalScoope

MagliettaColore = "Nera"
MagliettaPrezzo = 19.99
MagliettaQuantita = 3

Soma1 = (MagliettaPrezzo * MagliettaQuantita)

print(" ===========================================================") #LocalScoope
print("              Flusso di cassa operativo ")

print("Maglietta Colore: ", MagliettaColore)

print("Maglietta Prezzo: ", MagliettaPrezzo)

print("Maglietta Quantita", MagliettaQuantita)

print("Fatturazione futura ", Soma1)

print("===========================================================")

#Crea una variabile numero con valore 10. Stampa True se il numero è maggiore di 5, altrimenti False.

#GlobalScoope

Leone = 10
Uccello = 5

if Leone > Uccello:
    print("True, Leone ha piu forza di Uccello") #LocalScoope
else:
    print("False, Uccello non e piu forte di un Leone")

#Prova a combinare un int e un float: assegna a a = 5 e b = 2.5, poi calcola la loro somma.

#GlobalScoope

A = 5
B = 2.5

Soma2 = (A + B)
Soma3 = (Soma2 * 10 )


print("Convertitore da numeri decimali a numeri interi ", Soma2, "e il numero selezionato") #LocalScoope
print("Conversione completata con successo, il risultato e : ", Soma3)