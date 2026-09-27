kuhapituus = float(input("Anna kuhan pituus senttimetreinä: "))

if kuhapituus < 37:
    print(f"Laske kuha takaisin järveen. Kalan pituus on {37 - kuhapituus} senttimetriä liian vähän.")
else:
    print("Hieno kuha !")