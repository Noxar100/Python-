#nev kiiratas
def kosznev(nev):
    return "Szia " + nev + "!"

print(kosznev("Anna"))

#szor 2
def duplaz(szam):
    return szam * 2

print(duplaz(2))


#összead
def osszead(a, b):
    return a + b
print(osszead(40,50))


print("Python \n" * 3)


nevek = ["Anna", "Bela", "Edit", "Gabor"]

for nev in nevek:
    if nev.startswith("G"):
        print(nev)


import random

def game():
    szorny_hp = 100
    jatekos_hp = 100

    while szorny_hp > 0 and jatekos_hp > 0:
        sebzes = random.randint(14, 18)
        szorny_hp -= sebzes
        if szorny_hp < 0:
            szorny_hp = 0
        print(f"Megtámatad a szörnyet {sebzes} sebeztél szörny hp: {szorny_hp}")

        if szorny_hp > 0:
            sebzes = random.randint(14, 18)
            jatekos_hp -= sebzes
            if jatekos_hp < 0:
                jatekos_hp  = 0
            print(f"Megtámadtak {sebzes} sebzést kaptál {jatekos_hp} hp van")

    if szorny_hp == 0:
        print("Nyertél")
    else:
        print("Vesztettél") 
game()


#pontozás
pont  = int(input("add meg a pontszámod: "))

if pont <= 40:
    print("Elégtelen")
elif pont <= 60:
    print("Elégséges")
elif pont <= 80:
    print("Közepes")
elif pont < 90:
    print("Jó")
else:
    print("Jeles")


#számologep

szam1 = int(input("Add meg az eslö számot: "))
szam2 = int(input("Add meg az második számot: "))
muvelet = input("Add meg a müveletett (+ - * /): ")

if muvelet == "+":
    print(szam1 + szam2)
elif muvelet == "-":
    print(szam1 - szam2)
elif muvelet == "*":
    print(szam1 * szam2)
elif muvelet == "/":
    print(szam1 / szam2)
else:
    print("Helytelen müveletett adott meg")



def szamologep():
    szam1 = int(input("Add meg az eslö számot: "))
    szam2 = int(input("Add meg az második számot: "))
    muvelet = input("Add meg a müveletett (+ - * /): ")

    if muvelet == "+":
        print(szam1 + szam2)
    elif muvelet == "-":
        print(szam1 - szam2)
    elif muvelet == "*":
        print(szam1 * szam2)
    elif muvelet == "/":
        print(szam1 / szam2)
    else:
        print("Helytelen müveletett adott meg")

szamologep()


itezmeny = "Gábor Dénes Egyetem"

print(itezmeny[:5])
print(itezmeny[6:11])
print(itezmeny[12:])



szamlalo = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

while True:
    jegy = int(input("Add meg a jegyed (0 kilépés)"))

    if jegy == 0:
        break

    if jegy < 1 and jegy > 5:
        print("csak 1 és 5 kött adhatsz meg számot")
        continue

    szamlalo[jegy] += 1


tanulok = sum(szamlalo.values())
osszeg = sum(jegy * darab for jegy, darab in szamlalo.items())

print("tanulok száma", {tanulok})
print("5 ös tanulok", {szamlalo[5]})
print("4 est kapot", {szamlalo[4]})
print("3 ast kapot", {szamlalo[3]})
print("2 est kapot", {szamlalo[2]})
print("1 est kapot", {szamlalo[1]})


szam = int(input("Adjon meg egy pozitív számot: "))

if szam <= 0:
    print("Nem pozitív számot adott meg!")
else:
    osztok = []
    for i in range(1, szam + 1):
        if szam % i == 0:
            osztok.append(i)

    print(f"A(z) {szam} osztói: {osztok}")