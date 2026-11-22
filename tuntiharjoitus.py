hedelmat = {
    "omena": 0.54,
    "banaani": 0.67,
    "päärynä": 0.73,
    "mandariini": 0.39,
}

hedelma = input("Kerro hedelmän nimi: ")

if hedelma in hedelmat:
    print(hedelma, "hinta on", hedelmat[hedelma], "€/kpl")
else:
    print("Hedelmää ei löytynyt.")