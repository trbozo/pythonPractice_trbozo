# package Gun24;
#
# import java.util.HashMap;
# import java.util.Map;
#
# public class _02_Map {
#     public static void main(String[] args) {
#         HashMap<Integer, String> hm=new HashMap<>();
#         hm.put(1001, "Ismet Temur");
#         hm.put(1002, "Cihat Yılmaz");
#         hm.put(2001, "Talip Yıldız");
#         hm.put(5001, "Eyüpcan Bilgin");
#         hm.put(1002, "Hatice Bayrak"); // 1002 güncelleniyor
#
#         System.out.println("hm.keySet() = " + hm.keySet());
#         System.out.println("hm.values() = " + hm.values());
#
#         System.out.println();
#
#         for(Integer  k: hm.keySet())
#             System.out.println("k = " + k);
#
#         System.out.println();
#
#         for(String  v: hm.values())
#             System.out.println("v = " + v);
#
#         System.out.println();
#
#         for(Map.Entry<Integer,String> kv : hm.entrySet())
#             System.out.println(kv.getKey()+"-"+kv.getValue());
#
#
#
#
#     }
# }


def main():
    # HashMap benzeri bir Python sözlüğü oluşturma
    hm = {
        1001: "Ismet Temur",
        1002: "Cihat Yılmaz",
        2001: "Talip Yıldız",
        5001: "Eyüpcan Bilgin"
    }
    hm[1002] = "Hatice Bayrak"  # 1002 anahtarı güncelleniyor

    # Anahtarları ve değerleri yazdırma
    print("hm.keys() =", list(hm.keys()))
    print("hm.values() =", list(hm.values()))
    print()

    # Anahtarları tek tek yazdırma
    for k in hm:
        print("k =", k)
    print()

    # Değerleri tek tek yazdırma
    for v in hm.values():
        print("v =", v)
    print()

    # Anahtar-değer çiftlerini yazdırma
    for k, v in hm.items():
        print(f"{k}-{v}")

if __name__ == "__main__":
    main()


# Bu Python kodu, Java'da yapılan işlemleri takip eder:
#
# Sözlük oluşturma ve değerleri belirlerken, belirli bir anahtarın değerini güncelleme.
# .keys() ve .values() metodları ile anahtar ve değer listelerini yazdırma.
# Sözlük üzerinde döngü kullanarak anahtarları ve değerleri tek tek yazdırma.
# .items() metodu ile anahtar-değer çiftlerini döngüde kullanma.
# Python'da, HashMap'e benzer işlemler dictionary yapısı ile çok benzer şekilde gerçekleştirilir.