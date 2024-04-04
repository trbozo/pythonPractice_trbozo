# Kullanıcıdan "Fizik:90" gibi not bilgisini alın
# >= 90 için A
# >= 80 için B
# >= 70 için C
# >= 60 için D
# >= 40 için E
# < 40 için F yazdırın

not_bilgisi = input("Dersi ve notunu giriniz: ")  # Fizik:90

# Notu almak için iki yöntem var: ":" karakterinden sonra kalanı almak veya sadece sayıları almak
# İlk yöntem:
ogr_not = int(not_bilgisi.split(":")[1])

# İkinci yöntem:
ogr_not = int("".join(filter(str.isdigit, not_bilgisi)))

# Ladder if: merdivenli if
if ogr_not >= 90:
    print("A")
elif ogr_not >= 80:
    print("B")
elif ogr_not >= 70:
    print("C")
elif ogr_not >= 60:
    print("D")
elif ogr_not >= 40:
    print("E")
else:
    print("F")
