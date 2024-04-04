# package Gun05;
#
# import java.util.Scanner;
#
# public class _02_JavaScanner {
#     public static void main(String[] args) {
#
#         //tipi     adı      ilk değeri , arabalardan yeni araba
#         Scanner okuyucu = new Scanner(System.in);
#         // Bilgisayarlardan MyPc = yeni Bilgisayar();
#         // System.in  : klavyeden okuma görevi verildi okuyucuya
#
#         System.out.print("Sayi giriniz=");  // ne istendiği bilnsin diye yazıldı
#         int girilenSayi= okuyucu.nextInt(); // bu komutla sayı girilmesini bekliyor
#         //okuduğun sayıyı bana ver
#
#         System.out.println("girilenSayi = " + girilenSayi);
#         System.out.println("bitti");
#     }
# }



# Bu Java kodunun Python'a çevrilmiş hali:

# Scanner sınıfını kullanabilmek için gerekli kütüphaneyi ekleyelim
import sys

# Scanner nesnesini oluşturalım
okuyucu = sys.stdin

# Kullanıcıdan bir sayı isteyelim
print("Sayıyı giriniz=")
girilenSayi = int(input())  # Kullanıcıdan girdiyi okuyalım ve integera çevirelim

# Girilen sayıyı ekrana yazdıralım
print("Girilen sayı =", girilenSayi)
print("Bitti")


#Bu Python kodu, input() fonksiyonu kullanarak kullanıcıdan bir sayı girmesini isteyip, bu girişi alır ve bir değişkene atar. Daha sonra, girilen sayıyı ekrana yazdırır.






