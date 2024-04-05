# package Gun19;
#
# import java.util.Arrays;
# import java.util.Scanner;
#
# public class _03_Soru {
#     public static void main(String[] args) {
#         // Günün Sorusu :  3x2 lik bir diziyi kullanıcıdan sayı alarak
#         // doldurduktan sonra sadece tek elemenlarını tek boyutlu bir
#         // diziye atayınız.
#
#         Scanner oku=new Scanner(System.in);
#         int[][] tablo=new int[3][2]; // 3 satır 2 sütun
#         //kullanıcıdan dolduralım bunu
#
#         int tekMiktar=0;
#         for (int i = 0; i < tablo.length; i++) {
#
#             for (int j = 0; j < tablo[i].length; j++) {
#                 System.out.print("Sayı giriniz=");
#                 tablo[i][j]=oku.nextInt();
#
#                 if ( tablo[i][j] % 2 == 1)
#                     tekMiktar++;
#             }
#
#         }
#
#         //tablou yazdıralım, bakalım
#         System.out.println("0.Satır = " + Arrays.toString(tablo[0]));
#         System.out.println("1.Satır = " + Arrays.toString(tablo[1]));
#         System.out.println("2.Satır = " + Arrays.toString(tablo[2]));
#
#         //içindeki tek sayıları
#         int[] tekler=new int[tekMiktar];  // buna doldurun
#
#         int teklerIndex=0;
#         for (int i = 0; i < tablo.length; i++) {
#
#             for (int j = 0; j < tablo[i].length; j++)
#                 if ( tablo[i][j] % 2 == 1)
#                 {
#                     tekler[teklerIndex]=tablo[i][j];
#                     teklerIndex++;
#                 }
#         }
#
#         System.out.println("tekler = " + Arrays.toString(tekler));
#     }
# }

# Kullanıcıdan 3x2'lik bir dizi için sayı alıp doldurma
tablo = [[int(input("Sayı giriniz=")) for _ in range(2)] for _ in range(3)]

# Tek sayıları sayma
tek_miktar = sum(sayi % 2 == 1 for satir in tablo for sayi in satir)

# Tek sayıları bir listeye atama
tekler = [sayi for satir in tablo for sayi in satir if sayi % 2 == 1]

# Doldurulan tabloyu yazdırma
for i, satir in enumerate(tablo):
    print(f"{i}.Satır = {satir}")

# Tek sayıları içeren listeyi yazdırma
print("tekler =", tekler)


##Bu kod, ilk olarak kullanıcıdan 3x2'lik bir dizi doldurmak için sayı alır.
# Python list comprehension yapısı ile bu işlem sırasında ve sonrasında tek sayıları bulmak için kullanılır.
# Tek sayıların miktarı, bir generator expression ile sum() fonksiyonu kullanılarak hesaplanır ve sonrasında
# yine bir list comprehension ile tek sayılar ayrı bir listeye eklenir. Ardından, doldurulan tablo ve tek sayılar
# listesi ekrana yazdırılır.
# Bu yöntem, Java kodundaki döngüler ve koşullu ifadelerin Python'daki karşılığıdır ve daha sade bir kod yapısı sağlar.

