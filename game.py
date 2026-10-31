import random

jatek_hp = 100
szorny_hp = 100

while szorny_hp > 0 and jatek_hp > 0:

    # játékos támad
    sebzes = random.randint(14, 18)
    szorny_hp -= sebzes
    if szorny_hp < 0:
        szorny_hp = 0
    print(f"Te támadtál: {sebzes} sebzés. Szörny HP: {szorny_hp}")

    # szörny támad (csak ha még él)
    if szorny_hp > 0:
        sebzes = random.randint(12, 15)
        jatek_hp -= sebzes
        if jatek_hp < 0:
            jatek_hp = 0
        print(f"A szörny támadott: {sebzes} sebzés. Játékos HP: {jatek_hp}")

    print()

if szorny_hp == 0:
    print("Győztél!")
else:
    print("Vesztettél!")