kor = int(input("Add meg a korod: "))
nev = input("Add meg a neved: ")

while not kor > 6:
    print("Idősebbnek kell lenned, mint 6 éves!")
    kor = int(input("Add meg a korod: "))

while not len(nev) >= 3:
    print("A név-nek legalább 3 karakter hosszúnak kell lennie!")
    nev = input("Add meg újra a neved: ")

print("______________________________")
print(f"Korod: {kor}, Neved: {nev}.")