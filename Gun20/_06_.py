# package Gun20;
#
# import java.util.Arrays;
#
# public class _06_JavaMethod {
#     public static void main(String[] args) {
#         // mainde 20 elemanlı bir diziyi tanımlayınız, daha sonra bir fonksiyona
#         // göndererek random 100 e kadar olan sayılarla doldurunuz ve aynı fonksiyonda
#         // yazdırınız.
#
#         int[] dizi=new int[20];
#
#         diziDoldur(dizi);
#     }
#
#     public static void diziDoldur(int[] dizi){
#
#         for (int i = 0; i < dizi.length; i++)
#             dizi[i]=(int)(Math.random()*100);
#
#         System.out.println(Arrays.toString(dizi));
#     }
#
#
#
# }


import random

def dizi_doldur_ve_yazdir(dizi):
    for i in range(len(dizi)):
        dizi[i] = random.randint(0, 99)  # 0 ile 99 arası rastgele bir sayı üretir

    print(dizi)

def main():
    dizi = [0] * 20  # 20 elemanlı bir dizi tanımlama
    dizi_doldur_ve_yazdir(dizi)  # Diziyi doldur ve yazdır

if __name__ == "__main__":
    main()
