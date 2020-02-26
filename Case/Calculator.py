
val = int(input("Silahkan pilih = "))
a = int(input("masukan angka ke 1 = "))
b = int(input("masukan angka ke 2 = "))

def pilihan(val):
    switcher = {
        1: penambahan(a,b)
    }
    return switcher.get(val, "ga ada pilihan")


def penambahan(a, b):


    print( a + b)

#
# def pengurangan():
#     a = input("masukan angka ke 1")
#     b = input("masukan angka ke 2")
#     print("hasil pengurangan", a - b)
#
#
# def perkalian():
#     a = input("masukan angka ke 1")
#     b = input("masukan angka ke 2")
#     print("Hasil perkalian", a * b)
#
#
# def pembagian():
#     a = input("masukan angka ke 1")
#     b = input("masukan angka ke 2")
#     print("Hasil pembagian", a / b)

