import time
import sys
import msvcrt

def afficher_heure(heure, minute, seconde, mode_12_heures=False):
    format_heure = "{:02d}:{:02d}:{:02d}".format(heure % 12 if mode_12_heures else heure, minute, seconde)
    format_heure += " {}".format("AM" if heure < 12 else "PM") if mode_12_heures else ""
    sys.stdout.write("\r{}".format(format_heure))
    sys.stdout.flush()

def saisir_temps(message):
    heures = int(input(f"Entrez les heures de {message} : "))
    minutes = int(input(f"Entrez les minutes de {message} : "))
    secondes = int(input(f"Entrez les secondes de {message} : "))
    return heures, minutes, secondes

def affichage():
    return input("Choisissez le mode d'affichage (12 ou 24 heures) : ").lower() == "12"

def sonnerie_alarme(heure_actuelle, alarme):
    if heure_actuelle == alarme:
        print("C'est l'heure de se réveiller, dring dring !")
        sys.exit()

def pause():
    print("\nL'horloge est en pause. Appuyez sur Entrée pour la relancer.")
    while msvcrt.kbhit():
        msvcrt.getch()
    msvcrt.getch()

def main():
    heure, minute, seconde = saisir_temps("l'heure actuelle")
    alarme = saisir_temps("l'alarme")
    mode_12_heures = affichage()

    while True:
        afficher_heure(heure, minute, seconde, mode_12_heures)
        sonnerie_alarme((heure, minute, seconde), alarme)

        if msvcrt.kbhit() and msvcrt.getch() == b'\r':
            pause()

        time.sleep(1)
        seconde = (seconde + 1) % 60
        minute += 1 if seconde == 0 else 0
        heure = (heure + 1) % 24 if minute == 60 else heure

main()