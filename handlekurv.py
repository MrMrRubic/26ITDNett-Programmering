budsjett = 0
varer = []
priser = []
antall = []
totalt = 0


budsjett = float(input("Skriv budsjettet ditt (Kr): "))
while budsjett <= 0:
    print("Budsjettet kan ikke være lavere enn 1!")
    continue

while True:
    print("Skriv inn navn på varen du ønsker å kjøpe.\nØnsker du å fullføre og få kvittering skriver du \"ferdig\".")
    valg = str(input("Varenavn: "))
    if valg == "ferdig":
        break
    else:
        varer.append(valg)
        valg = float(input("Skriv pris per stk (Kr): "))
        while valg <= 0:
            print("Prisen må være større enn 0!")
            continue
        priser.append(valg)
        valg = int(input("Skriv antall varer: "))
        while valg >= 1:
            print("Antall må være minst 1!")
            continue
        antall.append(valg)

print(varer)
print(priser)
print(antall)