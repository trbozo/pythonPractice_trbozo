# package Gun20;
#
# import java.util.Arrays;
# import java.util.Scanner;
#
# public class _07_JavaMethod {
#     public static void main(String[] args) {
#         // Kullanıcı ile 5 elemanlı bir diziyi main de doldurduktan sonra,
#         // dizinin en küçük, en büyük elemanını ve
#         // ortalamasını ayrı fonksiyonlarda bulup yazdırınız
#
#         Scanner oku= new Scanner(System.in);
#         int[] dizi=new int[5];
#
#         for (int i = 0; i < dizi.length; i++) {
#             System.out.print("Sayı giriniz=");
#             dizi[i]=oku.nextInt();
#         }
#
#         System.out.println(Arrays.toString(dizi));
#
#         enBuyukYaz(dizi);
#         enKucukYaz(dizi);
#         ortalamaYaz(dizi);
#     }
#
#     public static void enBuyukYaz(int[] dizi){
#         Arrays.sort(dizi);
#         System.out.println("En büyük="+dizi[dizi.length-1]);
#     }
#
#     public static void enKucukYaz(int[] dizi){
#         Arrays.sort(dizi);
#         System.out.println("En küçük="+dizi[0]);
#     }
#
#     public static void ortalamaYaz(int[] dizi){
#
#         int toplam=0;
#         for (int i = 0; i < dizi.length; i++)
#             toplam= toplam+dizi[i];
#
#         int ort=toplam/dizi.length;
#
#         System.out.println("ort = " + ort);
#     }
#
#
#
# }


def en_buyuk_yaz(dizi):
    print("En büyük =", max(dizi))

def en_kucuk_yaz(dizi):
    print("En küçük =", min(dizi))

def ortalama_yaz(dizi):
    ortalama = sum(dizi) / len(dizi)
    print("Ortalama =", ortalama)

def main():
    dizi = [int(input("Sayı giriniz: ")) for _ in range(5)]
    print(dizi)

    en_buyuk_yaz(dizi)
    en_kucuk_yaz(dizi)
    ortalama_yaz(dizi)

if __name__ == "__main__":
    main()
