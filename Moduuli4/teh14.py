import random

oikea = random.randint(1, 10)
arvaus = 0

while arvaus != oikea:
    arvaus = int(input("Arvaa luku väliltä 1–10: "))
    if arvaus > oikea:
        print("Liian suuri")
    elif arvaus < oikea:
        print("Liian pieni")
    else:
        print("Oikein")