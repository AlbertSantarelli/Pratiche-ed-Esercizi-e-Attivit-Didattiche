#Programma by Albert Santarelli
#Esercizi e sorgenti - Esercizi Variabili, tipi di dati e Casting

def sfida_1():
    nome = "Albert Santarelli"
    eta = 27
    citta = "Torino"

    print(nome, eta, citta)


def sfida_2():
    x = 12
    print(x)

    x = 25
    print(x)


def sfida_3():
    x = 18
    y = 32

    print("Somma:", x + y)


def sfida_4():
    x = 45
    y = 20

    x, y = y, x

    print(x, y)


def sfida_5():
    base = 8
    altezza = 14

    area = base * altezza

    print("Area rettangolo:", area)


def sfida_6():
    a = 25
    b = 4.8

    print(a + b)


def sfida_7():
    x, y, z = 15, 35, 50

    media = (x + y + z) / 3

    print("Media:", media)


def sfida_8():
    s1 = "Ad Albert piace "
    s2 = "giocare a basket"

    print(s1 + s2)


def sfida_9():
    print("Benvenuto! " * 3)


def sfida_10():
    a = 25
    b = 50
    c = 75

    print(a < b)
    print(b > c)
    print(a < c)


def sfida_11():
    x = 35

    y = float(x)

    print(y)


def sfida_12():
    n = "7825"

    s = int(n)

    print("Il numero è:", s)


def sfida_13():
    print(bool(25))
    print(bool(0))
    print(bool(-50))
    print(bool(""))
    

# MENU PRINCIPALE

while True:

    print("\n==============================")
    print("        MENU DELLE SFIDE")
    print("==============================")

    print("1  - Nome, età e città")
    print("2  - Modifica variabile")
    print("3  - Somma")
    print("4  - Scambio variabili")
    print("5  - Area rettangolo")
    print("6  - Somma int + float")
    print("7  - Media")
    print("8  - Concatenazione stringhe")
    print("9  - Ripetizione stringa")
    print("10 - Operatori di confronto")
    print("11 - Conversione float")
    print("12 - Conversione int")
    print("13 - Valori booleani")
    print("0  - Esci")

    scelta = input("\nScegli una sfida: ")

    if scelta == "1":
        sfida_1()

    elif scelta == "2":
        sfida_2()

    elif scelta == "3":
        sfida_3()

    elif scelta == "4":
        sfida_4()

    elif scelta == "5":
        sfida_5()

    elif scelta == "6":
        sfida_6()

    elif scelta == "7":
        sfida_7()

    elif scelta == "8":
        sfida_8()

    elif scelta == "9":
        sfida_9()

    elif scelta == "10":
        sfida_10()

    elif scelta == "11":
        sfida_11()

    elif scelta == "12":
        sfida_12()

    elif scelta == "13":
        sfida_13()

    elif scelta == "0":
        print("Programma terminato. Arrivederci!")
        break

    else:
        print("Scelta non valida!")

    input("\nPremi INVIO per continuare...")


#Materie studiate a integrazione dell'esercizio
    #https://docs.python.org/it/3/library/stdtypes.html?utm_source=
    #https://docs.python.org/it/3/library/functions.html?utm_source=