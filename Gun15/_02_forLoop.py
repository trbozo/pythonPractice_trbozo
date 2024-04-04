# package Gun15;
#
# import java.util.Scanner;
#
# public class _02_forLoop {
#     public static void main(String[] args) {
#         // kullanıcının gireceği iki sayı arasındaki sayıların
#         // toplamını bulunuz.
#
#         Scanner oku = new Scanner(System.in);
#         System.out.print("Birinci sayı=");
#         int sayi1 = oku.nextInt();
#
#         System.out.print("İkinci sayı=");
#         int sayi2 = oku.nextInt();
#
#         int toplam = 0;
#         for(int i = sayi1; i <= sayi2; i++)
#              toplam += i;
#
#         System.out.println("Toplam = " + toplam);
#     }
# }

sayi1 = int(input("Birinci sayı="))
sayi2 = int(input("İkinci sayı="))

toplam = 0
for i in range(sayi1, sayi2 + 1):
    toplam += i

print("Toplam =", toplam)
