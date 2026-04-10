# Data
nama = ["Asep", "Budi", "Cecep"]
nilai = [
    [50, 70, 40, 80],
    [78, 78, 80, 65],
    [57, 88, 67, 69]
]

# Mahasiswa terpintar
tertinggi = 0
nama_terbaik = ""

for i in range(3):
    total = 0
    for n in nilai[i]:
        total += n
    rata = total / 4

    if rata > tertinggi:
        tertinggi = rata
        nama_terbaik = nama[i]

# Mata kuliah terkecil
mk1 = (50 + 78 + 57) / 3
mk2 = (70 + 78 + 88) / 3
mk3 = (40 + 80 + 67) / 3
mk4 = (80 + 65 + 69) / 3

terkecil = mk1
mk = 1

if mk2 < terkecil:
    terkecil = mk2
    mk = 2
if mk3 < terkecil:
    terkecil = mk3
    mk = 3
if mk4 < terkecil:
    terkecil = mk4
    mk = 4

# Output
print("Mahasiswa Terpintar:", nama_terbaik, "(Nilai:", round(tertinggi, 2), ")")
print("Mata kuliah Nilai Terkecil: MK", mk, "(Nilai:", round(terkecil, 2), ")")