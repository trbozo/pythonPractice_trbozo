# package Gun05;
#
# import jdk.nashorn.internal.runtime.OptimisticReturnFilters;
#
# public class _01_Ornek1 {
#     public static void main(String[] args) {
#         String ad="İsmet Temur";
#         int sinifNo=5;
#         char subesi='A';
#         boolean gectiMi=true;
#
#         System.out.println(ad+" "+sinifNo+" "+subesi+" "+gectiMi);
#         // birleştirmeye soldan sağa doğru giderim.
#         // solda string varsa yanındaki otomatik stringe dönüştürürüm yani eklerim
#
#         System.out.println("merhaba"+1+2); // merhaba12
#         System.out.println(1+2+"merhaba"); // 3merhaba
#         // soldan geldiğinden önce 1+2 3 olarak TOPLAMA işlemi yaptı, sonrasında
#         // merhaba stringine gelince ona EKLENDİ
#
#         // sayıları Stringe nasıl çeviririz ?
#         int sayi=56;
#         String strSayi= String.valueOf(sayi); // sayıyı string çevirmiş oldun
#     }
# }


# Bu Java kodunun Python'a çevrilmiş hali:

# Değişkenleri tanımlayalım
ad = "İsmet Temur"
sinifNo = 5
subesi = 'A'
gectiMi = True

# Değişkenleri birleştirip ekrana yazdıralım
print(ad, sinifNo, subesi, gectiMi)
# birleştirmeye soldan sağa doğru giderim.
# solda string varsa yanındaki otomatik stringe dönüştürürüm yani eklerim

# String birleştirme işlemi
print("merhaba" + str(1) + str(2))  # merhaba12
print(str(1 + 2) + "merhaba")  # 3merhaba
# soldan geldiğinden önce 1+2 3 olarak TOPLAMA işlemi yaptı, sonrasında
# merhaba stringine gelince ona EKLENDİ

# Sayıyı stringe çevirme işlemi
sayi = 56
strSayi = str(sayi)  # sayıyı string çevirmiş oldun


#Bu Python kodu, verilen değişkenlerin birleştirilmesini ve sayının bir stringe dönüştürülmesini gösterir. Python'da, değişkenleri birleştirmek için + operatörünü kullanabilir ve sayıları stringe dönüştürmek için str() fonksiyonunu kullanabilirsiniz.






