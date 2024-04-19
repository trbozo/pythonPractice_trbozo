# package Gun24;
#
# import java.util.HashMap;
# import java.util.LinkedHashMap;
# import java.util.Map;
# import java.util.TreeMap;
#
# public class _03_Map {
#     public static void main(String[] args) {
#         // HashMap : hızlı çalışmak için , kendi algoritmasına göre sırada saklar
#         // LinkedHashMap : eklendiği sıraya göre içindeki elemanları saklar
#         // TreeMap : içideki elemanları herzaman KEY e göre sıralı saklar
#
#         HashMap<Integer, String> hm=new HashMap<>();
#         hm.put(9,"tilki");
#         hm.put(2,"kedi");
#         hm.put(30,"köpek");
#         hm.put(11,"kuş");
#         hm.put(4,"kurt");
#
#         System.out.println("hm = " + hm);
#
#         LinkedHashMap<Integer, String> lhm=new LinkedHashMap<>();
#         lhm.put(9,"tilki");
#         lhm.put(2,"kedi");
#         lhm.put(30,"köpek");
#         lhm.put(11,"kuş");
#         lhm.put(4,"kurt");
#
#         System.out.println("lhm = " + lhm);
#
#         TreeMap<Integer, String> tm=new TreeMap<>();
#         tm.put(9,"tilki");
#         tm.put(2,"kedi");
#         tm.put(30,"köpek");
#         tm.put(11,"kuş");
#         tm.put(4,"kurt");
#
#         System.out.println("tm = " + tm);
#
#
#
#
#     }
# }


# Python'da, Java'daki HashMap, LinkedHashMap ve TreeMap gibi farklı Map uygulamalarına karşılık gelen yapılar
# genellikle sözlükler (dict) ve bazı özel kütüphanelerle sağlanır. Python'daki standart sözlük (dict),
# Python 3.7'den itibaren sıralıdır (yani LinkedHashMap gibi davranır). Sıralı bir sözlük (OrderedDict) daha eski
# Python sürümleri için collections modülünde mevcuttur. TreeMap benzeri bir yapıya ihtiyaç duyulduğunda ise
# sortedcontainers modülündeki SortedDict kullanılabilir.

from collections import OrderedDict
from sortedcontainers import SortedDict

def main():
    # HashMap benzeri bir Python sözlüğü (Python 3.7 ve sonrası için sıralıdır)
    hm = {
        9: "tilki",
        2: "kedi",
        30: "köpek",
        11: "kuş",
        4: "kurt"
    }
    print("hm =", hm)

    # LinkedHashMap benzeri bir Python sözlüğü (eski Python sürümleri için)
    lhm = OrderedDict()
    lhm[9] = "tilki"
    lhm[2] = "kedi"
    lhm[30] = "köpek"
    lhm[11] = "kuş"
    lhm[4] = "kurt"
    print("lhm =", lhm)

    # TreeMap benzeri bir yapı (anahtarlar otomatik olarak sıralanır)
    tm = SortedDict()
    tm[9] = "tilki"
    tm[2] = "kedi"
    tm[30] = "köpek"
    tm[11] = "kuş"
    tm[4] = "kurt"
    print("tm =", tm)

if __name__ == "__main__":
    main()

# Bu kod örneğinde:
#
# dict: Standart Python sözlüğü kullanılıyor ve Python 3.7 ve sonrasında sıralı olarak değerleri tutuyor.
# OrderedDict: collections modülünden OrderedDict kullanarak, eski Python sürümlerinde elemanların eklenme sırasını koruyan bir yapı sağlanıyor.
# SortedDict: sortedcontainers modülünden SortedDict kullanarak, anahtarlara göre otomatik olarak sıralanan bir yapı sağlanıyor.
# Eğer sortedcontainers yüklü değilse, terminal veya komut satırında pip install sortedcontainers komutu ile kurulum yapılabilir.






