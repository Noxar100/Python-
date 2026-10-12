
import os
import time
import msvcrt
import random

szelesseg = 20
magassag = 10

kigyo = [(5, 4), (4, 4), (3, 4)]
etel = (12, 4)

irany = (1, 0)
pont = 0

while True:

    # Billentyuzet kezelese
    if msvcrt.kbhit():
        billeny = msvcrt.getch()

        if billeny in (b'\x00', b'\xe0'):
            billeny = msvcrt.getch()

            if billeny == b'H' and irany != (0, 1):
                irany = (0, -1)
            elif billeny == b'P' and irany != (0, -1):
                irany = (0, 1)
            elif billeny == b'K' and irany != (1, 0):
                irany = (-1, 0)
            elif billeny == b'M' and irany != (-1, 0):
                irany = (1, 0)

    os.system("cls")

    # Palya kirajzolasa
    for y in range(magassag):
        sor = ""

        for x in range(szelesseg):
            if (x, y) == kigyo[0]:
                sor += "@"
            elif (x, y) in kigyo:
                sor += "o"
            elif (x, y) == etel:
                sor += "*"
            else:
                sor += " "

        print("|" + sor + "|")

    print("Pontszam:", pont)
    print("Iranyitas: nyilak")

    # Uj fej kiszamitasa
    fej_x, fej_y = kigyo[0]
    dx, dy = irany

    uj_fej = (fej_x + dx, fej_y + dy)
    uj_x, uj_y = uj_fej

    # Falnak utkozes
    if (uj_x < 0 or uj_x >= szelesseg
            or uj_y < 0 or uj_y >= magassag):
        print("Vege a jateknak!")
        break

    
    
    eszik = uj_fej == etel
    
    kigyo.insert(0, uj_fej)
    
    if eszik: 
        pont += 10
        
        szabad_helyek = [
            (x, y)
            for x in range(szelesseg)
            for y in range(magassag)
            if(x, y) not in kigyo
        ]
        
        if not szabad_helyek:
            print("Gratulálok megtelt a pálya")
            break
        
        etel = random.choice(szabad_helyek)
    else:
        kigyo.pop()

    
    
    
    

    time.sleep(0.3)
    

print("Jatek vege!")
print("Elért Pontszámod:", pont)

