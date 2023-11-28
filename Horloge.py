import time
import sys
import msvcrt

def afficher_heure(heure, minute, seconde, mode_12_heures=False):
    if mode_12_heures:
        am_pm = "AM" if heure < 12 else "PM"
        heure_12h = heure % 12 if heure % 12 != 0 else 12
        sys.stdout.write(f"\r{heure_12h:02d}:{minute:02d}:{seconde:02d} {am_pm}")
    else:
        sys.stdout.write(f"\r{heure:02d}:{minute:02d}:{seconde:02d}")
    sys.stdout.flush()

def regler_heure():
    heures = int(input("Entrez les heures : "))
    minutes = int(input("Entrez les minutes : "))
    secondes = int(input("Entrez les secondes : "))
    return heures, minutes, secondes

def regler_alarme():
    heures_alarme = int(input("Entrez l'heure de l'alarme : "))
    minutes_alarme = int(input("Entrez les minutes de l'alarme : "))
    secondes_alarme = int(input("Entrez les secondes de l'alarme : "))
    return heures_alarme, minutes_alarme, secondes_alarme

def affichage():
    mode = input("Choisissez le mode d'affichage (12 ou 24 heures) : ").lower()
    return mode == "12"

def verifier_alarme(heure_actuelle, alarme):
    if heure_actuelle == alarme:
        print(" C'est l'heure de ce réveiller, dring dring !")
        sys.exit()

def mettre_en_pause():
    print("\nL'horloge est en pause. Appuyez sur Entrée pour la relancer.")
    while msvcrt.kbhit():
        msvcrt.getch()
    msvcrt.getch()

def main():
    heure, minute, seconde = regler_heure()
    alarme = regler_alarme()
    mode_12_heures = affichage()
    while True:
        afficher_heure(heure, minute, seconde, mode_12_heures)
        verifier_alarme((heure, minute, seconde), alarme)
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\r':
                mettre_en_pause()
        time.sleep(1)
        seconde += 1
        if seconde == 60:
            seconde = 0
            minute += 1
            if minute == 60:
                minute = 0
                heure += 1
                if heure == 24:
                    heure = 0

if __name__ == "__main__":
    main()