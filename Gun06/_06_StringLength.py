# package Gun06;
#
# public class _06_StringLength {
#     public static void main(String[] args) {
#         // StringLength  -> bir Stringin uzunluğunu verir.(Kaç tane harf var)
#
#         String cumle="Bugün hava çok yağmurlu"; //boşluk da bir harf gibidir.
#
#         int uzunluk=cumle.length(); // cumlenin içindeki değerin kaç harf olduğunu verir
#
#         System.out.println("uzunluk = " + uzunluk);
#         System.out.println("uzunluk2 = " + cumle.length()); // 2.seçenek
#     }
# }


# Java kodunun Python'a dönüştürülmüş hali

# StringLength  -> bir Stringin uzunluğunu verir.(Kaç tane harf var)

cumle = "Bugün hava çok yağmurlu"  # boşluk da bir harf gibidir.

uzunluk = len(cumle)  # cumlenin içindeki değerin kaç harf olduğunu verir

print("uzunluk =", uzunluk)
print("uzunluk2 =", len(cumle))  # 2.seçenek



#Bu Python kodu, bir stringin uzunluğunu (kaç karakterden oluştuğunu) hesaplar ve yazdırır. len() fonksiyonu, bir stringin uzunluğunu döndürür.






