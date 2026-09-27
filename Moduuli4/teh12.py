tuumat = float(input("Kerro tuumamäärä: "))
while tuumat >= 0:
    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {sentit:.2f} cm")
    tuumat = float(input("Kerro tuumamäärä: "))
print("Ohjelma loppuu.")