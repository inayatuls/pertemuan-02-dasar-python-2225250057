"""
Nama: Inayatul Sholihah
NIM: 2225250057
Kelas: 3A
"""
print("KALKULATOR KOORDINAT DUA TITIK")
x1 = float(input("x titik A: "))
y1 = float(input("y titik A: "))
x2 = float(input("x titik B: "))
y2 = float(input("y titik B: "))
dx = x2 - x1
dy = y2 - y1
jarak = (dx ** 2 + dy ** 2) ** 0.5
titik_tengah = ((x1 + x2) / 2, (y1 + y2) / 2)
print(f"Titik A : ({x1:.2f}, {y1:.2f})")
print(f"Titik B : ({x2:.2f}, {y2:.2f})")
print(f"Perubahan : dx = {dx:.2f}, dy = {dy:.2f}")
print(f"Jarak A ke B : {jarak:.2f}")
print(f"Titik tengah : ({titik_tengah[0]:.2f}, {titik_tengah[1]:.2f})")
