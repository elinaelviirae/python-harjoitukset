def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa = summa + luku
    return summa
 
lista = [3, 7, 12, 5, 8]
print(f"Listan {lista} summa on {laske_summa(lista)}.")