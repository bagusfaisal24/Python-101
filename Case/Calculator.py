list = list(("1. Penambahan", "2. Pengurangan", "3. Perkalian", "4. Pembagian"))
print(list)
val = int(input("Silahkan pilih Opsi = "))
a = int(input("masukan angka ke 1 = "))
b = int(input("masukan angka ke 2 = "))


def penambahan(a, b):
    return a + b


def pengurangan(a, b):
    return a - b


def perkalian(a, b):
    return a * b


def pembagian(a, b):
    return a / b


if val == int(1):
    print(a, "ditambah", b, "=", penambahan(a, b))
elif val == int(2):
    print(a, "dikurangi", b, "=", pengurangan(a, b))
elif val == int(3):
    print(a, "dikali", b, "=", perkalian(a, b))
elif val == int(4):
    print(a, "dibagi", b, "=", pembagian(a, b))
else:
    print("Pilihan anda tidak ada")
