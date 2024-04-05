# package Gun20;
#
# import java.util.Scanner;
#
# public class _09_JavaMethod {
#     public static void main(String[] args) {
#         // Kullanıcının gireceği 2 sayıdan büyük olanını bulma işlemini bir metodda
#         // yaptıktan sonra main de yazdırınız.
#
#         Scanner oku = new Scanner(System.in);
#
#         System.out.print("1.Sayı=");
#         int sayi1 = oku.nextInt();
#
#         System.out.print("2.Sayı=");
#         int sayi2 = oku.nextInt();
#
#         //int enb=Math.max(sayi1,sayi2);
#
#         int enb= enbBul(sayi1,sayi2); // veri alır, veri döndürür
#         System.out.println("enb = " + enb);
#     }
#
#     public static int enbBul(int s1, int s2){
#         return (s1 > s2 ? s1 : s2);
#     }
#
#
# }


def enb_bul(s1, s2):
    # İki sayı arasından büyük olanı döndürür
    return max(s1, s2)

def main():
    # Kullanıcının gireceği iki sayıdan büyük olanını bulup yazdırma
    sayi1 = int(input("1. Sayı= "))
    sayi2 = int(input("2. Sayı= "))

    enb = enb_bul(sayi1, sayi2)  # Veri alır, veri döndürür
    print("enb =", enb)

if __name__ == "__main__":
    main()
