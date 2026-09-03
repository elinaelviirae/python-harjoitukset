kanta = float(input("Kerro suorakulmiolle kanta: "))
korkeus = float(input("Kerro suorakulmiolle korkeus: "))

piiri = 2 * (kanta + korkeus)
pinta_ala = kanta * korkeus

print("Suorakulmion piiri on " + str(piiri) + " cm")
print("Suorakulmion pinta-ala on " + str(pinta_ala) + " cm²")