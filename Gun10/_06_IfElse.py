# // package Gun10;
# //
# // import java.util.Scanner;
# //
# // public class _06_IfElse {
# //     public static void main(String[] args) {
# //
# //         // Girilen bir öğrenci notuna göre 50 den büyük eşit ise geçtiniz.
# //         // küçük ise kaldınız yazdırınız.
# //
# //         Scanner oku = new Scanner(System.in);
# //         System.out.print("Notu giriniz=");
# //         int ogrNot = oku.nextInt();
# //
# //         // 1.yöntem bilgisayar boş yere yoruluyor
# //         if (ogrNot >= 50)
# //             System.out.println("Geçtiniz, Tebrikler");
# //
# //         if (ogrNot < 50) {
# //             System.out.println("üzgünüz, kaldınız");
# //             System.out.println("yaz okuluna bekleriz");
# //         }
# //
# //         // 2.Yöntem olması gereken
# //         if (ogrNot >=50)
# //             System.out.println("tebrikler");
# //         else //yukarı şart değilse
# //             System.out.println("kaldınız");
# //
# //     }
# // }
# //
# // // {} parantezlerini herzaman kullanabilirsiniz ,
# // // ancak if şartı sağlandığında çalışacak tek bir komut var ise
# // // kullanmak zorunlu değildir.


ogr_not = int(input("Notu giriniz="))

# 1.yöntem bilgisayar boş yere yoruluyor
if ogr_not >= 50:
    print("Geçtiniz, Tebrikler")
if ogr_not < 50:
    print("Üzgünüz, kaldınız")
    print("Yaz okuluna bekleriz")

# 2.Yöntem olması gereken
if ogr_not >= 50:
    print("Tebrikler")
else:  # Yukarıdaki şart değilse
    print("Kaldınız")


##Bu Python kodu, girilen bir öğrenci notuna göre "50'den büyük eşit ise geçtiniz,
# küçük ise kaldınız" şeklinde sonuç verir. Python'da if-else yapısını kullanarak,
# kodu daha etkin ve okunabilir bir hale getirebiliriz. Yukarıdaki örnek, Java'daki
# if-else yapısının Python'daki karşılığını göstermektedir.
# Python'da, kullanıcıdan veri almak için input() fonksiyonu kullanılır ve
# girilen değer int() fonksiyonu ile tam sayıya dönüştürülür.
