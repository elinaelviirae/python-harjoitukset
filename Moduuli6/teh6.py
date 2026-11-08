import math

def yksikkohinta(halkaisija, hinta):
    pinta_ala = math.pi * halkaisija ** 2
    hinta / pinta_ala

halkaisija1 = input("Anna pizzan halkaisija: ")
hinta1 = input("Anna pizzan hinta: ")