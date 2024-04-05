# package Gun21;
#
# import java.util.ArrayList;
# import java.util.Scanner;
#
# public class _06_ArrayList_Soru {
#     public static void main(String[] args) {
#         // Bir öğretmenden girmek istediği kadar notu alınız,
#         // Öğretmene devam etmek istiyormusunuz (E/H) şeklinde sorunuz
#         // ve ortalamayı geçen öğrenci sayısını bulunuz.
#
#         Scanner okuInt=new Scanner(System.in);
#         Scanner okuStr=new Scanner(System.in);
#
#         ArrayList<Integer> notlar=new ArrayList<>();
#         int toplam=0;
#         String cevap="";
#         do{
#             //notu oku
#             System.out.print("Not giriniz=");
#             int not= okuInt.nextInt();
#
#             //ArrayList e ekle
#             notlar.add(not);
#             toplam=toplam+not;
#
#             System.out.print("Devam etmek istiyor musunuz?(E/H)=");
#             //Cevabı al döngü şartı olarak kullan
#             cevap= okuStr.next();
#
#         }while(cevap.equalsIgnoreCase("E")); // evet olduğu sürece dön
#
#         System.out.println("notlar = " + notlar);
#
#         int ort= toplam / notlar.size();
#         System.out.println("ort = " + ort);
#
#         int gecenSayisi=0;
#         for (int i = 0; i < notlar.size(); i++) {
#             if (notlar.get(i) >= ort)
#                 gecenSayisi++;
#         }
#
#         System.out.println("gecenSayisi = " + gecenSayisi);
#
#
#
#
#
#
#
#     }
# }


#Python'da Liste ve Döngüler Kullanarak Not Ortalaması ve Geçen Öğrenci Sayısını Hesaplama

def main():
    notlar = []
    toplam = 0
    cevap = "E"

    while cevap.upper() == "E":
        # Notu oku
        notu = int(input("Not giriniz: "))
        # Liste'ye ekle
        notlar.append(notu)
        toplam += notu

        # Devam etmek isteyip istemediğini sor
        cevap = input("Devam etmek istiyor musunuz? (E/H): ")

    print("Notlar:", notlar)

    ort = toplam / len(notlar)
    print("Ortalama:", ort)

    # Ortalamayı geçen öğrenci sayısını hesapla
    gecen_sayisi = sum(1 for notu in notlar if notu >= ort)
    print("Geçen öğrenci sayısı:", gecen_sayisi)

if __name__ == "__main__":
    main()


#Python'da, sum() fonksiyonu ile birlikte kullanılan generator expression (sum(1 for notu in notlar if notu >= ort)),
# koşulu sağlayan
# her not için 1 ekleyerek toplamı hesaplamamızı sağlar ve böylece ortalama notu geçen öğrenci sayısını bulmamıza yardımcı olur.