# package Gun21;
#
# import java.util.ArrayList;
# import java.util.Arrays;
# import java.util.Scanner;
#
# public class _05_ArrayList_Soru {
#     public static void main(String[] args) {
#         // Kullanıcıdan alacağınız 6 elemanlı(sayı) bir dizinin
#         // sadece tek sayı olan elemanlarını ayrı diziye(liste)(ArrayList) atayarak
#         // yazdırınız.
#
#         Scanner oku = new Scanner(System.in);
#         int[] dizi=new int[6];
#
#         for (int i = 0; i < dizi.length; i++) {
#             System.out.print("Sayı=");
#             dizi[i]=oku.nextInt();
#         }
#
#         System.out.println("dizi = " + Arrays.toString(dizi));
#
#         ArrayList<Integer> tekler=new ArrayList<>();
#
#         for (int i = 0; i < dizi.length; i++) {
#
#             if (dizi[i] % 2 == 1)
#                 tekler.add(dizi[i]);
#         }
#
#         //1.yol fotoğraf
#         System.out.println("tekler = " + tekler);
#
#         //2.yol tek tek elemanları
#         for (int i = 0; i < tekler.size(); i++)
#             System.out.print(tekler.get(i)+"\t");
#
#     }
# }


def main():
    # Kullanıcıdan 6 sayı alıp bir listeye atama
    dizi = [int(input("Sayı giriniz: ")) for _ in range(6)]
    print("Dizi:", dizi)

    # Tek sayıları bulup başka bir listeye ekleme
    tekler = [sayi for sayi in dizi if sayi % 2 == 1]

    # Tek sayıların listesini yazdırma
    print("Tekler:", tekler)

    # Tek sayıları tek tek yazdırma
    for sayi in tekler:
        print(sayi, end="\t")

if __name__ == "__main__":
    main()


#List comprehension ([sayi for sayi in dizi if sayi % 2 == 1]),
# Python'da diziler üzerinde döngüler kullanarak ve belirli bir koşulu sağlayan elemanları seçerek yeni
# bir liste oluşturmanın kısa ve okunaklı bir yoludur.
# Bu kod, temel liste işlemlerini ve koşullu eleman seçimini göstermektedir.