# Otopark ücretleri: (Ternary operatör ile yapınız.)
# 3 saate kadar 50 tl, 5 saate kadar 100 tl, 5 den büyükse 120 tl'dir.
# Kullanıcıdan kaç saat kaldığını alarak ücreti yazdırınız

saat = int(input("Saat: "))

# String olarak
str_ucret = "50 tl" if saat < 3 else ("100 tl" if saat < 5 else "120 tl")
print("strUcret =", str_ucret)

# int olarak
ucret = 50 if saat < 3 else (100 if saat < 5 else 120)
print("ucret =", ucret, "tl")
