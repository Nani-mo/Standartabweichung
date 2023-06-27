print("It's a trap")
import math

# Eingabe der Werte
def eingabe():    
    argumente_liste = [float(item) for item in input("Gib Argumente ein (mit Leerzeichen abtrennen): ").split()]
    prozentsatz_liste = [float(item) for item in input("Gib Prozentsaetze ein (mit Leerzeichen abtrennen): ").split()]
    return argumente_liste, prozentsatz_liste

# eingabe ueberpruefen
def verify(argumente_liste, prozentsatz_liste):
    laenge_argumente = len(argumente_liste); laenge_prozentsatz = len(prozentsatz_liste)
    if laenge_argumente != laenge_prozentsatz:
        print("jedem Argument muss ein Prozentsatz zugeordnet werden und andersrum genauso!!!")
        eingabe()
    return laenge_argumente

# Berechnen der vom Erwartungswert, Varianz und Standartabweichung
def calc(argumente_liste, prozentsatz_liste, laenge_argumente):
    print("---------------------------------------------------")

    erwartungswert = 0                                                                         # Erwartungswert berechnen
    for i in range(laenge_argumente):                                                          #
        erwartungswert = argumente_liste[i] * prozentsatz_liste[i] + erwartungswert            #
    print("Erwartungswert: ", erwartungswert)                                                  #

    i = 0; Varianz = 0                                                                         # Varianz berechnen
    for i in range(laenge_argumente):                                                          #
        Varianz = (argumente_liste[i] - erwartungswert) ** 2 * prozentsatz_liste[i] + Varianz  #
    print("Varianz: ", Varianz)                                                                #

    Standartabweichung = math.sqrt(Varianz)                                                    # Standartabweichung berechnen
    print("Staandarttabweichung: ", Standartabweichung)                                        #
    print("---------------------------------------------------")
    
def main():
    print("Das Programm berechnet die Standartabweichung von en eingegebenden Werten")
    argumente_liste, prozentsatz_liste = eingabe()
    laenge_argumente = verify(argumente_liste, prozentsatz_liste)
    calc(argumente_liste, prozentsatz_liste, laenge_argumente)
    useless = str(input("\n\nEnter zum beenden"))

try:
    main()
except KeyboardInterrupt:
    exit()

