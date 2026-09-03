import random

kolmenkoodi = "".join(str(random.randint(0, 9)) for _ in range(3))

neljankoodi = "".join(str(random.randint(1, 6)) for _ in range(4))

print("Kolmenumeroinen lukon koodi: " + kolmenkoodi)
print("Neljänumeroinen lukon koodi: " + neljankoodi)