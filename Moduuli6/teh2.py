import random
  
def heita_noppaa(tahkot):
    return random.randint(1, tahkot)
 
tahkoja = int(input("Anna nopan tahkojen määrä: "))
tulos = 0
while tulos != tahkoja:
    tulos = heita_noppaa(tahkoja)
    print(tulos)
 