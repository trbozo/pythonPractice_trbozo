# package Gun25._01_Ornek;
#
# // tiplerin yani class ların tanımlandığı yer
#
# import java.util.ArrayList;
# import java.util.Scanner;
#
# public class _01_JavaClassAndObject {
#
#     // method
#     public static void main(String[] args) {
#         //ana method : programın başladığı ve bittiği yer
#         int sayi;
#         Scanner oku=new Scanner(System.in);
#         ArrayList<Integer> liste=new ArrayList<>();
#
#         Araba benimArabam=new Araba();
#         benimArabam.renk="kırmızı";
#         benimArabam.yili=2024;
#         benimArabam.motorHacmi=1600;
#         benimArabam.marka="Togg";
#
#         System.out.println("benimArabam.marka = " + benimArabam.marka);
#         System.out.println("benimArabam.yili = " + benimArabam.yili);
#         System.out.println("benimArabam.motorHacmi = " + benimArabam.motorHacmi);
#         System.out.println("benimArabam.renk = " + benimArabam.renk);
#     }
#     //metod
# }
#
# // tiplerin yani class ların tanımlandığı yer
# class Araba {
#     String renk;
#     int yili;
#     String marka;
#     int motorHacmi;
# }


class Araba:
    def __init__(self, renk, yili, marka, motor_hacmi):
        self.renk = renk
        self.yili = yili
        self.marka = marka
        self.motor_hacmi = motor_hacmi


def main():
    # Araba nesnesi oluşturma ve özelliklerini belirleme
    benim_arabam = Araba("kırmızı", 2024, "Togg", 1600)

    # Araba bilgilerini yazdırma
    print("benim_arabam.marka =", benim_arabam.marka)
    print("benim_arabam.yili =", benim_arabam.yili)
    print("benim_arabam.motor_hacmi =", benim_arabam.motor_hacmi)
    print("benim_arabam.renk =", benim_arabam.renk)


if __name__ == "__main__":
    main()


# Python'da sınıf tanımlamak için class anahtar kelimesi kullanılır.
# Her sınıfın bir başlatıcı (__init__) metodu olabilir, bu metod nesne oluşturulduğunda çağrılır.
# self kelimesi, sınıf içerisindeki metotların ve özelliklerin bu sınıfa ait olduğunu belirtir.
#
# Yukarıdaki Python kodu, Java'daki işlevselliği aynı şekilde gerçekleştirir: bir Araba nesnesi oluşturur,
# özelliklerini atar ve bu özellikleri ekrana yazdırır.