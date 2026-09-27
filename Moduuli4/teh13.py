pienin = None
suurin = None

annettuluku = input("Anna luku: ")
while annettuluku != "":
    luku = int(annettuluku)
    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku
    annettuluku = input("Anna luku: ")
else:
    print(f"Pienin luku: {pienin} Suurin luku: {suurin}")