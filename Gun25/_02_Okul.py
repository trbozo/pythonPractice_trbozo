# // Bir
# okulda
# kayıt
# programı
# için
# Ogrenci
# bilgilerini
# alan
# modül
# // yazılacaktır.Ogrenci
# ye
# ait
# bilgiler(okulNo, adi, soyadi, sinifi
# ve
# adres) vardır.
# // bu
# yapıyı
# oluşturunuz.
# // Daha
# sonra
# bi
# öğrenci
# tanımlayıp
# değerlerini
# verip
# yazdırınız


# package Gun25._02_Ornek;
#
# public class Okul {
#     public static void main(String[] args) {
#         Ogrenci ogr1=new Ogrenci();
#         ogr1.okulNo=1001;
#         ogr1.adi="Kaan";
#         ogr1.soyadi="Gül";
#         ogr1.adresi="Üsküdar";
#         ogr1.sinifi=12;
#
#         System.out.println("ogr1.okulNo = " + ogr1.okulNo);
#         System.out.println("ogr1.adi = " + ogr1.adi);
#         System.out.println("ogr1.soyadi = " + ogr1.soyadi);
#         System.out.println("ogr1.sinifi = " + ogr1.sinifi);
#         System.out.println("ogr1.adresi = " + ogr1.adresi);
#     }
# }
#
# class Ogrenci{
#     int okulNo;
#     String adi;
#     String soyadi;
#     int sinifi;
#     String adresi;
# }

class Ogrenci:
    def __init__(self, okul_no, adi, soyadi, sinifi, adresi):
        self.okul_no = okul_no
        self.adi = adi
        self.soyadi = soyadi
        self.sinifi = sinifi
        self.adresi = adresi


def main():
    # Ogrenci nesnesi oluşturma ve özelliklerini belirleme
    ogr1 = Ogrenci(1001, "Kaan", "Gül", 12, "Üsküdar")

    # Ogrenci bilgilerini yazdırma
    print("ogr1.okul_no =", ogr1.okul_no)
    print("ogr1.adi =", ogr1.adi)
    print("ogr1.soyadi =", ogr1.soyadi)
    print("ogr1.sinifi =", ogr1.sinifi)
    print("ogr1.adresi =", ogr1.adresi)


if __name__ == "__main__":
    main()


# Python'da, sınıf tanımlamak için class anahtar kelimesi kullanılır ve her sınıfın bir başlatıcı (__init__) metodu olabilir.
# Bu metod nesne oluşturulduğunda çağrılır. self kelimesi, sınıf içerisindeki metotların ve özelliklerin bu sınıfa ait olduğunu belirtir
# . Yukarıdaki Python kodu, Java'daki işlevselliği aynı şekilde gerçekleştirir: bir Ogrenci nesnesi oluşturur,
# özelliklerini atar ve bu özellikleri ekrana yazdırır.






