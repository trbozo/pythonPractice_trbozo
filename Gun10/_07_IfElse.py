# package Gun10;
#
# import java.util.Scanner;
#
# public class _07_IfElse {
#     public static void main(String[] args) {
#         // Girilen bir sayının tek mi çift mi olduğunu yazdırınız.
#
#         Scanner oku=new Scanner(System.in);
#
#         System.out.println("Sayi=");
#         int sayi=oku.nextInt();
#
#         //1.yöntem
#         int kalan= sayi % 2;
#
#         if (kalan==0)
#             System.out.println("Çift sayı");
#         else
#             System.out.println("tek sayı");
#
#         //2.yöntem
#         if (sayi%2 ==0)
#             System.out.println("Çift sayı");
#         else
#             System.out.println("tek sayı");
#     }
# }

sayi = int(input("Sayi="))

# 1.yöntem
kalan = sayi % 2

if kalan == 0:
    print("Çift sayı")
else:
    print("Tek sayı")

# 2.yöntem
if sayi % 2 == 0:
    print("Çift sayı")
else:
    print("Tek sayı")


##Bu Python kodu, girilen bir sayının tek mi çift mi olduğunu kontrol eder ve sonucu ekrana yazdırır. Java'daki Scanner sınıfıyla kullanıcıdan veri alma işlevselliğine benzer şekilde, Python'da input() fonksiyonu kullanılır ve girilen değer int() fonksiyonu ile tam sayıya dönüştürülür. Kod, Java'daki iki yöntemi de içerir: ilk yöntemde, sayının 2 ile bölümünden kalan hesaplanır ve kalan 0 ise sayı çift, değilse tek olarak kabul edilir; ikinci yöntemde, doğrudan sayının 2 ile bölümünden kalanın kontrolü yapılır.
