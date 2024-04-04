# package Gun06;
#
# public class _07_StringCharAt {
#     public static void main(String[] args) {
#         // charAt(index) ; istenen noktadaki karakteri verir
#         //                      111
#         //            0123456789012
#         String cumle="Merhaba Dünya"; // uzunluk 13
#         System.out.println("cumle.length() = " + cumle.length());
#
#         char ilkHarf=cumle.charAt(0); // 0 oda numaralı , yani indexli karakter
#         System.out.println("ilkHarf = " + ilkHarf);
#     }
# }


# Java kodunun Python'a dönüştürülmüş hali

# charAt(index) ; istenen noktadaki karakteri verir
#                      111
#            0123456789012
cumle = "Merhaba Dünya"  # uzunluk 13
print("len(cumle) =", len(cumle))

ilkHarf = cumle[0]  # 0 oda numaralı , yani indexli karakter
print("ilkHarf =", ilkHarf)


#Bu Python kodu, bir stringin belirli bir indeksteki karakterini döndürür. Python'da, bir stringi indeksleme işlemi yaparak belirli bir karaktere erişebilirsiniz. İndeksler 0'dan başlar, bu yüzden ilk karaktere erişmek için [0] kullanılır. len() fonksiyonu, bir stringin uzunluğunu döndürür.






