sukupuoli = input("Sukupuolesi (nainen/mies): ")

if sukupuoli != "nainen" and sukupuoli != "mies":
    print("Virheellinen sukupuoli.")
else:
    hgarvo = float(input("Mikä on hemoglobiiniarvosi (g/l): "))

    if sukupuoli == "nainen":
        if hgarvo < 117:
            print("Hemoglobiiniarvosi on alhainen.")
        elif hgarvo > 175:
            print("Hemoglobiiniarvosi on korkea.")
        else:
            print("Hemoglobiiniarvosi on normaali.")
    elif sukupuoli == "mies":
        if hgarvo < 134:
            print("Hemoglobiiniarvosi on alhainen.")
        elif hgarvo > 195:
            print("Hemoglobiiniarvosi on korkea.")
        else:
            print("Hemoglobiiniarvosi on normaali.")
    