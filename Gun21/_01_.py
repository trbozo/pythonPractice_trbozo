# package Gun21;
#
# import java.util.Scanner;
#
# public class _01_JavaMethod {
#     public static void main(String[] args) {
#         // kullanıcının gireceği bir sayıya kadar olan sayıların toplamını
#         // bir fonksiyonda buldurup mainden yazdırınız
#         // 5 -> 1+2+3+4+5
#
#         Scanner oku=new Scanner(System.in);
#         System.out.print("Bir sayı giriniz=");
#         int sayi=oku.nextInt();
#
#         int toplam= toplamBul(sayi); // Math.Max(4,5);
#
#         System.out.println("toplam = " + toplam);
#     }
#
#     public static int toplamBul(int sayi)
#     {
#         int toplam=0;
#         for (int i = 1; i <= sayi; i++) {
#             toplam = toplam + i;
#         }
#
#         return toplam;
#     }
# }


def toplam_bul(sayi):
    # Belirtilen sayıya kadar olan sayıların toplamını bulur
    toplam = sum(range(1, sayi + 1))
    return toplam

def main():
    # Kullanıcının gireceği sayıya kadar olan sayıların toplamını bulur ve yazdırır
    sayi = int(input("Bir sayı giriniz: "))
    toplam = toplam_bul(sayi)
    print("Toplam =", toplam)

if __name__ == "__main__":
    main()


# toplam_bul fonksiyonu belirtilen sayıya kadar olan sayıların toplamını hesaplar ve sonucu döndürür.
# range(1, sayi + 1) fonksiyonu, 1'den başlayıp girilen sayıya kadar (sayı dahil) olan sayıları bir aralık olarak üretir
# ve sum fonksiyonu bu sayıların toplamını hesaplar.
# 
# main fonksiyonu kullanıcıdan bir sayı alır, toplam_bul fonksiyonunu çağırarak
# bu sayıya kadar olan sayıların toplamını bulur ve sonucu yazdırır. Bu yapı,
# kodun modüler ve okunabilir olmasını sağlar. if __name__ == "__main__": ifadesi,
# bu Python dosyası doğrudan çalıştırıldığında main fonksiyonunun çağrılmasını sağlar.