# package Gun23;
#
# import java.util.HashSet;
# import java.util.LinkedHashSet;
# import java.util.TreeSet;
#
# public class _03_Sets {
#     public static void main(String[] args) {
#         // SETS : TEKRAR YOK
#         // HashSet : HIZLI, bunun için içidekileri kendi mantığına sıralar
#         // LinkedHashSet : EKLENME SIRASI na göre sıralı tutar
#         // TreeSet : HERZAMAN SIRALI, kendinden sortlu
#
#         // Hızlı, bunun için kendine bör algoritmayla sıralı tutuyor
#         HashSet<String> hs = new HashSet<>();
#         hs.add("bir");
#         hs.add("iki");
#         hs.add("üç");
#         hs.add("dört");
#         hs.add("beş");
#         System.out.println("hs = " + hs);
#
#         // Ekleme SIRASI na göre dısralı tutar
#         LinkedHashSet<String> lhs = new LinkedHashSet<>();
#         lhs.add("bir");
#         lhs.add("iki");
#         lhs.add("üç");
#         lhs.add("dört");
#         lhs.add("beş");
#         System.out.println("lhs = " + lhs);
#
#         // Kendin sortlu
#         TreeSet<String> ts = new TreeSet<>();
#         ts.add("üç");
#         ts.add("dört");
#         ts.add("beş");
#         ts.add("bir");
#         ts.add("iki");
#         System.out.println("ts = " + ts);
#
#
#     }
# }


# Bu Java kodu, Set interface'inin üç farklı uygulamasını (HashSet, LinkedHashSet ve TreeSet) kullanarak nasıl çalıştıklarını
# ve aralarındaki farkları gösterir. Bu uygulamalar, tekrar eden elemanları barındırmazlar ancak elemanların saklanma sıraları
# ve sıralama davranışları farklılık gösterir:
#
# HashSet: En hızlı performansı sunar ancak elemanlar sırasız bir şekilde saklanır.
# İçeriklerin saklanma sırası Java'nın kendi algoritmasına bağlıdır ve tahmin edilemez.
#
# LinkedHashSet: Elemanları ekleme sırasına göre sıralı tutar. Performansı HashSete göre
# biraz daha düşüktür ama ekleme sırasının korunması gerektiğinde idealdir.
#
# TreeSet: Elemanları doğal sıralama düzenine (alfabetik veya sayısal) göre saklar.
# Sıralı erişim gerektiğinde kullanılır fakat bu sıralama işlemi nedeniyle performansı,
# HashSet ve LinkedHashSete göre daha düşük olabilir.
#
# Python'da set yapısı, HashSete benzer şekilde tekrar eden elemanları barındırmaz ve
# elemanlar sırasız bir şekilde saklanır. Ancak Python'da LinkedHashSet ve TreeSete doğrudan
# karşılık gelen yapılar yoktur. Yine de benzer davranışları elde etmek için sıralı dict (Python 3.7 ve sonrası)
# veya collections.OrderedDict (sıralı tutma) ve sorted() fonksiyonu (sıralama için) kullanılabilir.
#
# Python'da benzer bir örnek vermek gerekirse:

# HashSet benzeri
hs = {"bir", "iki", "üç", "dört", "beş"}
print("hs =", hs)

# Python'da LinkedHashSet benzeri doğrudan bir yapı yok ama sıralı dict kullanılabilir:
lhs = {"bir": None, "iki": None, "üç": None, "dört": None, "beş": None}
print("lhs =", list(lhs.keys()))

# TreeSet benzeri
ts = sorted({"üç", "dört", "beş", "bir", "iki"})
print("ts =", ts)


# Bu Python kodu, set yapısını kullanarak HashSet benzeri bir örnek ve sorted() fonksiyonu
# ile TreeSet benzeri sıralı bir liste oluşturur. Python'da LinkedHashSete tam bir karşılık olmadığı için,
# sıralı bir dict kullanarak ve anahtarları bir listeye dönüştürerek ekleme sırasını koruyabiliriz.