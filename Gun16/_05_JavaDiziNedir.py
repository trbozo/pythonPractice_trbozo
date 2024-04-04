# package Gun16;
#
# public class _05_JavaDiziNedir {
#     public static void main(String[] args) {
#         int sayi;  // 1 tane sayı saklamak için
#
#         int ogrNot=0;
#
#         int ogrNot1;
#         int ogrNot2;
#         //..
#         //..
#         int ogrNot50=50;
#
#         // 1 tanımlamada yani 1 kalemde çoklu veri tutabilecek
#         // değişkenler lazım
#         int[] notlar=new int[50]; // içide 50 tane sayı saklayabilen değişken
#
#         notlar[0]=50;
#         notlar[1]=70;
#         //..
#         //..
#         notlar[49]=89;
#
#
#         System.out.println("notlar[0], 1. Öğrenci notu ="+ notlar[0]);
#         System.out.println("50. yani,notlar[49],son öğrencini notu = "+ notlar[49]);
#         System.out.println("kaç not var ? = " + notlar.length);
#     }
# }


# Python'da listeler, Java'daki dizilerin işlevselliğini sağlar.
# Liste oluşturulurken boyut belirtmeye gerek yoktur.

# Öğrenci notlarını saklamak için bir liste oluşturuyoruz.
notlar = []

# Liste içine öğrenci notlarını ekliyoruz.
notlar.append(50)  # 1. öğrenci notu
notlar.append(70)
# ...
# ...
notlar.append(89)  # 50. öğrenci notu

# Listeden öğrenci notlarını alıp ekrana yazdırıyoruz.
print("notlar[0], 1. Öğrenci notu =", notlar[0])
print("50. yani, notlar[49], son öğrencinin notu =", notlar[49])
print("kaç not var ? =", len(notlar))


#Bu Python kodu, öğrenci notlarını saklamak için bir liste kullanır.
# Liste oluşturulurken boyut belirlemeye gerek yoktur ve .append() metoduyla listeye yeni öğeler eklenir.
# len() fonksiyonu kullanılarak listenin uzunluğu alınabilir.






