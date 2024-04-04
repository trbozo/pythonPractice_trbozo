# package Gun10;
#
# import java.util.Scanner;
#
# public class _08_MantiksalIfadeler {
#     public static void main(String[] args) {
#         // mantıksal ifadeler
#         // ve     &&
#         // veya   ||
#
#         // Soru : girilen bir sayı 0 dan büyük ve 100 den küçük eşit
#         // ise geçerli not , değil ise geçerli olmayan not
#         Scanner oku=new Scanner(System.in);
#
#         System.out.print("ogrNot=");
#         int ogrNot=oku.nextInt();
#
#         if ( 0<ogrNot && ogrNot<=100 )
#             System.out.println("Geçerli not");
#         else
#             System.out.println("Geçerli değil");
#     }
# }


ogr_not = int(input("ogrNot="))

if 0 < ogr_not and ogr_not <= 100:
    print("Geçerli not")
else:
    print("Geçerli değil")


#kullanıcıdan alınan öğrenci notunun geçerli olup olmadığını kontrol eder. Notun 0'dan büyük ve 100'e eşit veya küçük olup olmadığına bakar ve buna göre "Geçerli not" veya "Geçerli değil" çıktısını verir. Java'daki && mantıksal operatörü, Python'da aynı şekilde and anahtar kelimesi ile kullanılır. Kullanıcıdan veri almak için Python'da input() fonksiyonu kullanılır ve int() fonksiyonu ile bu veri tam sayıya dönüştürülür.