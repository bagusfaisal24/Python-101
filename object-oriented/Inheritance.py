class Mahasiswa:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def getMahasiswa(self):
        return "Mahasiswa bernama {} asal {}".format(self.nama, self.asal)


class Universitas(Mahasiswa):
    def kampus(self):
        return "UAD"


emp = Mahasiswa("Bagus", "Tegal")
print(emp.nama, emp.asal)

emp2 = Universitas("Bagus", "Tegal")
print(emp2.nama, emp2.asal, "Kuliah di", emp2.kampus())
