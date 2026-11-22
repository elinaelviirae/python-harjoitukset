lentoasemat = {
    "XAAA": "Helsinki",
    "XBBB": "Oulu",
    "XCCC": "Rovaniemi"
}

while True:
    print("1 = uusi lentoasema, 2 = hae, 3 = lopeta")
    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        koodi = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[koodi] = nimi
        print("Lentoasema tallennettu.")
    elif valinta == "2":
        koodi = input("Anna ICAO-koodi: ").upper()
        if koodi in lentoasemat:
            print(lentoasemat[koodi])
        else:
            print("Lentoasemaa ei löytynyt.")
    elif valinta == "3":
        print("Ohjelma päättyy.")