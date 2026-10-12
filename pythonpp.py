beker = int(input("Adj meg egy számot: "))

if beker % 2 == 0:
    print("Páros")
else:
    print("Páratlan")



# számoló gép


szam1 = int(input("Add meg az elsö számot: "))
szam2 = int(input("Add meg a második számot: "))
muvelet = input("Adj meg egy muveletett (+, -, *, /): ")


if muvelet == "+":
    print(szam1 + szam2)
elif muvelet == "-":
    print(szam1 - szam2)
elif muvelet == "*":
    print(szam1 * szam2)   
elif muvelet == "/":
    print(szam1 / szam2)   
else:
    print("Hibás művelet") 



# eletkor


eletkor = int(input("Add meg az életkorod: "))

if eletkor <= 5:
    print("Kisgyerek")
elif eletkor <= 18:
    print("Gyerek")
elif eletkor <= 65:
    print("Felnöt")
else:
    print("idös")
    
    
#def feladat

def terulet(szelesseg, magassag):
    ter = szelesseg * magassag
    return ter

szelesseg = float("Add meg a szélességet")
magassag = float("Add meg a Magasság")

eredmeny = terulet(szelesseg, magassag)
print(f"A téglalap területe {eredmeny}")