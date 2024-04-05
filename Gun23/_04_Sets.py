# package Gun23;
#
# import java.util.Iterator;
# import java.util.TreeSet;
#
# public class _04_Sets {
#     public static void main(String[] args) {
#         TreeSet<String> renkler=new TreeSet<>();
#         renkler.add("Red");
#         renkler.add("Green");
#         renkler.add("Blue");
#         renkler.add("Red");
#         renkler.add("RED");
#
#         //Ekrana yazdırma (fotoğraf)
#         System.out.println("renkler = " + renkler);
#
#         //Ekrana tek tek nasıl yazdırırım
#         for(String eleman: renkler) // sıra garanti değil
#             System.out.println("eleman = " + eleman);
#
# //        int[] dizi={34,5,6,7,8,89,899,77};
# //        for(int eleman : dizi)
# //            System.out.println("eleman = " + eleman);
#
#         //SETLERİ hafızadaki sırasına göre nasıl garanti olarak alırdım ?
#         Iterator gosterge=renkler.iterator(); // renklerin başına konumlandı
#         while (gosterge.hasNext()) // sıradaki eleman var ise
#         {
#             System.out.println("renkler = " + gosterge.next());
#             // sıradaki eleman
#             // .Next gostergenin gösterdiği elemanı temsil ediyor
#         }
#
#
#
#
#
#
#
#
#     }
# }

# Bu Java kodu, TreeSet kullanarak bir renkler koleksiyonu oluşturur ve bu koleksiyon içindeki elemanları çeşitli yollarla ekrana yazdırır. TreeSet, elemanları doğal sıralama düzenine göre saklar ve tekrar eden elemanları kabul etmez. Bu yüzden "Red" sadece bir kez saklanır, ancak "RED" farklı bir eleman olarak kabul edilir çünkü büyük/küçük harf duyarlıdır.
#
# Kodda elemanları yazdırmanın üç yolu gösterilir:
#
# Doğrudan TreeSetin toString() metodunu kullanarak bütün koleksiyonu bir kere de yazdırmak.
# Gelişmiş for döngüsü kullanarak elemanları tek tek yazdırmak.
# Bir Iterator kullanarak koleksiyonun elemanlarını sırasıyla yazdırmak. Iterator, koleksiyon üzerinde döngü yaparken elemanları silmek gibi daha esnek işlemler yapılmasına olanak tanır.
# Python'da, set yapısı HashSete benzer şekilde çalışır ve sıralı bir koleksiyon olmadığı için TreeSetin Python'daki doğrudan bir karşılığı yoktur. Ancak, sıralı bir sete ihtiyaç duyulduğunda sorted fonksiyonu kullanılabilir. İşte benzer bir Python kodu:

renkler = {"Red", "Green", "Blue", "Red", "RED"}

# Ekrana yazdırma
print("renkler =", renkler)

# Ekrana tek tek nasıl yazdırırım
for eleman in sorted(renkler):  # sıralı yazdırma
    print("eleman =", eleman)

# Python'da Iterator kullanımı genellikle gerekli değildir çünkü
# for döngüsü ve diğer yüksek seviye fonksiyonlar çoğu ihtiyacı karşılar.
# Ancak, iter ve next fonksiyonları ile benzer bir davranış elde edilebilir:
gosterge = iter(sorted(renkler))  # renklerin sıralı bir şekilde göstergesi
while True:
    try:
        print("renkler =", next(gosterge))
    except StopIteration:
        break  # Iterator sona erdiğinde döngüden çık



