OIKEA_TUNNUS = "kissafani95"
OIKEA_SALASANA = "koira123"

kirjautumistiedotok = True

while kirjautumistiedotok:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")
    if tunnus == OIKEA_TUNNUS and salasana == OIKEA_SALASANA:
        kirjautumistiedotok = True
        print("Tervetuloa!")
    else:
        print("Pääsy evätty!")

