# package Gun17;
#
# import java.util.Scanner;
#
# public class _01_JavaArray {
#     public static void main(String[] args) {
#         // 50 kişilik bir sınıfın notlarını giriniz ve ortalamadan büyük
#         // kaç not olduğunu bulunuz ve bunları yazdırnız.
#
#         Scanner oku=new Scanner(System.in);
#         int[] notlar=new int[50]; //50 tane int sayi gibi
#
#         int notToplam=0; // burada veri girişi ve not toplamı yapılıyor
#         for(int i=0;i< notlar.length ; i++) {
#             System.out.print("Not giriniz=");
#             notlar[i] = oku.nextInt();
#
#             notToplam=notToplam+notlar[i];
#         }
#
#         int ort= notToplam/notlar.length;  // ortalama bulunuyor
#         System.out.println("ort = " + ort);
#
#         int gecenler=0; // aşağıda geçen sayısı ve geçen notlar bulunyor
#         for(int i=0;i< notlar.length ; i++) {
#             if (notlar[i] >= ort) {
#                 System.out.println("notlar[i] = " + notlar[i]);
#                 gecenler++;
#             }
#         }
#
#         System.out.println("gecenler = " + gecenler);
#     }
#
# }

# 50 kişilik bir sınıfın notlarını giriniz ve ortalamadan büyük kaç not olduğunu bulunuz
# ve bunları yazdırınız.

# 50 öğrencinin notlarını almak için boş bir liste oluşturuyoruz.
notlar = []

# Kullanıcıdan 50 öğrencinin notlarını girişlerini alıyoruz ve listeye ekliyoruz.
notToplam = 0
for i in range(50):
    notlar.append(int(input("Not giriniz=")))
    notToplam += notlar[i]

# Notların ortalamasını hesaplıyoruz.
ort = notToplam / len(notlar)
print("Ortalama =", ort)

# Ortalamadan büyük notları ve sayılarını buluyoruz ve yazdırıyoruz.
gecenler = 0
for not_sayisi in notlar:
    if not_sayisi >= ort:
        print("Not:", not_sayisi)
        gecenler += 1

print("Ortalamadan büyük notların sayısı:", gecenler)

