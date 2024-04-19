from Ogrenci import Ogrenci

def main():
    ogr1 = Ogrenci(2001, "Cilem", "Okkali", 12, "Kadıköy")

    print("ogr1.okulNo =", ogr1.okul_no)
    print("ogr1.ad =", ogr1.ad)
    print("ogr1.soyad =", ogr1.soyad)
    print("ogr1.sinif =", ogr1.sinif)
    print("ogr1.adres =", ogr1.adres)

if __name__ == "__main__":
    main()