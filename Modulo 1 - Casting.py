#Programma by Albert Santarelli
#Chieda all’utente di inserire un numero intero.
#Converta questo numero in numero decimale (float) e lo stampi.
#Converta lo stesso numero in stringa e lo stampi insieme a un messaggio.


#===============================Importazioni================================= #GlobalScoope

import sys 
import time 

#colori
Verde = "\033[92m" 
Rosso = "\033[91m" 
Normale = "\033[0m" 
Giallo = "\033[93m" 

#===============================Configurazione Principali================================= #GlobalScoope

Nomeutente = str(input(f"{Giallo}Come vorresti essere chiamato ? : {Normale}")) 
print (f"{Giallo}Benvenuti,{Normale} {Nomeutente} {Giallo},al sistema di conversione dei tipi di dati !{Normale}") 
Iniziato = f"{Verde}Sistema caricato con successo.{Normale}" 
Carica = f"{Giallo}Inizializzazione del sistema{Normale}" 
Tipo1 = f"{Rosso}Str{Normale}" 
Tipo2 = f"{Rosso}Int{Normale}" 
Tipo3 = f"{Rosso}Float{Normale}" 
Selezione = "Seleziona il formato in cui desideri convertire." 
Menu_Selezione = f"1 = {Tipo1} , 2 = {Tipo2} , 3 = {Tipo3} ." 

#===============================Configurazione Secondaria================================= #GlobalScoope

print (Carica,f"[{Verde}-                                        {Normale}]") 
time.sleep(2)
print (Carica,f"[{Verde}----                                     {Normale}]")
time.sleep(2)
print (Carica,f"[{Verde}-------                                  {Normale}]")
time.sleep(2)
print (Carica,f"[{Verde}----------------                         {Normale}]")
time.sleep(2)
print (Carica,f"[{Verde}------------------                       {Normale}]")
time.sleep(3)
print (Carica,f"[{Verde}-----------------------                  {Normale}]")
time.sleep(3)
print (Carica,f"[{Verde}---------------------------              {Normale}]")
time.sleep(5)
print (Carica,f"[{Verde}--------------------------------         {Normale}]")
time.sleep(2)
print (Carica,f"[{Verde}--------------------------------------   {Normale}]")
time.sleep(3)
print (Carica,f"[{Verde}-----------------------------------------{Normale}]")
time.sleep(5)
print (Iniziato)

Num = int(input(f"{Giallo}Inserisci uno numero intero : {Normale}")) 
Num_Int = int(Num) 
Num_Float = float(Num_Int) 
Num_Str = str(Num_Float) 

print (Selezione)
print (Menu_Selezione)

#===============================Configurazione Del Menu================================= #GlobalScoope

while True:
    Num_Menu_Selezione = (input (f"{Giallo}Selezionare l'opzione desiderata oppure digitare{Rosso} ''uscire'' {Giallo}per chiudere il programma : {Normale}")).strip()

    if Num_Menu_Selezione.lower() == "uscire":
        print(f"{Rosso}Il programma è stato chiuso con successo{Normale}")
        sys.exit()

    if Num_Menu_Selezione == "1":
        print (f"{Giallo}Hai selezionato l'opzione:{Rosso} Str {Normale}")
        print(f"{Verde}Numero convertito con successo !{Normale}", Num_Str)
        print(f"{Giallo}Controllo di sicurezza{Rosso}", type(Num_Str))

    elif Num_Menu_Selezione == "2":
        print (f"{Giallo}Hai selezionato 2'opzione:{Rosso} Int {Normale}")
        print(f"{Verde}Numero convertito con successo !{Normale}", Num_Int)
        print(f"{Giallo}Controllo di sicurezza{Rosso}", type(Num_Int))

    elif Num_Menu_Selezione == "3":
        print (f"{Giallo}Hai selezionato 3'opzione:{Rosso} Float {Normale}")
        print(f"{Verde}Numero convertito con successo !{Normale}", Num_Float)
        print(f"{Giallo}Controllo di sicurezza{Rosso}", type(Num_Float))

    else:
        print ("{Giallo}Selezionare un'opzione o digitare {Rosso}''uscire'' {Giallo}per chiudere il programma.{Normale}")



