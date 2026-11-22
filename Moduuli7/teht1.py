vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    print(f"Kuukausi {kuukausi} on {vuodenajat[kuukausi - 1]}.")
else:
    print("Virhe. Vuodessa on vaan 12 kuukautta")