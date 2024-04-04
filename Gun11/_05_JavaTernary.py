# package Gun11;
#
# import java.util.Scanner;
#
# public class _05_JavaTernary {
#     public static void main(String[] args) {
#         //Soru: Girilen sayı 50 den büyük ise "Büyük" , değilse "Değil" değerini
#         // ekrana yazdırınız. Ternary operatör ile yapınız.
#
#         Scanner oku=new Scanner(System.in);
#         System.out.print("Sayı giriniz=");
#         int sayi= oku.nextInt();
#
#         String sonuc= sayi > 50 ? "Büyük" : "Değil";
#
#         System.out.println("sonuc = " + sonuc);
#
#         //int intSonuc= sayi > 50 ? 1 : 0;
#         //boolean booleanSonuc= sayi > 50 ? true : false;
#     }
#
#
# }


# Soru: Girilen sayı 50 den büyük ise "Büyük", değilse "Değil" değerini
# ekrana yazdırınız. Ternary operatör ile yapınız.

sayi = int(input("Sayı giriniz: "))

sonuc = "Büyük" if sayi > 50 else "Değil"

print("sonuc =", sonuc)

# İkinci bir örnek:
# intSonuc = 1 if sayi > 50 else 0
# booleanSonuc = True if sayi > 50 else False
