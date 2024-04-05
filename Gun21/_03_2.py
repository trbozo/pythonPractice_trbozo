# package Gun21;
#
# public class _03_JavaMethod_2 {
#     public static void main(String[] args) {
#         int s1=4;
#         int s2=12;
#         int s3=12;
#         int s4=12;
#
#         int sonuc1=toplamBul(s1,s2);
#         int sonuc2=toplamBul(s1,s2,s3);
#         int sonuc3=toplamBul(s1,s2,s3,s4);
#         int sonuc4=toplamBul(s1,s2,s3,s4,67);
#         System.out.println("sonuc1 = " + sonuc1);
#         System.out.println("sonuc2 = " + sonuc2);
#         System.out.println("sonuc3 = " + sonuc3);
#         System.out.println("sonuc4 = " + sonuc4);
#     }
#
#     // kaç tane gelirse gelsin, hepsini diziye atıp işleme alınabilir
#     public static int  toplamBul(int... dizi){
#         int toplam=0;
#
#         for (int i = 0; i < dizi.length; i++)
#            toplam=toplam+dizi[i];
#
#         return toplam;
#     }
#
# }


def toplam_bul(*dizi):
    # *dizi, fonksiyona verilen tüm parametreleri bir tuple olarak alır
    return sum(dizi)  # dizi içindeki tüm elemanların toplamını döndürür


def main():
    s1 = 4
    s2 = 12
    s3 = 12
    s4 = 12

    sonuc1 = toplam_bul(s1, s2)
    sonuc2 = toplam_bul(s1, s2, s3)
    sonuc3 = toplam_bul(s1, s2, s3, s4)
    sonuc4 = toplam_bul(s1, s2, s3, s4, 67)

    print(f"sonuc1 = {sonuc1}")
    print(f"sonuc2 = {sonuc2}")
    print(f"sonuc3 = {sonuc3}")
    print(f"sonuc4 = {sonuc4}")


if __name__ == "__main__":
    main()
