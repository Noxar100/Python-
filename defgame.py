import random

def game():
    szorny_hp = 100
    jatekos_hp = 100

    while szorny_hp > 0 and jatekos_hp > 0:
    
        sebzes = random.randint(14,20)
        szorny_hp -= sebzes
        if szorny_hp < 0:
            szorny_hp = 0
        print(f"Megtámatad a szörnyet {sebzes} sebzes {szorny_hp} szörny hp ja")
           
        if szorny_hp > 0:
            sebzes = random.randint(12, 15)
            jatekos_hp -= sebzes
            if jatekos_hp < 0:
                jatekos_hp = 0
            print(f"Megtámadtak: {sebzes} sebzés, {jatekos_hp} HP maradt")

        if szorny_hp == 0:
            print("Gyöztél")
        else:
            print("Vesztettél")
game() 