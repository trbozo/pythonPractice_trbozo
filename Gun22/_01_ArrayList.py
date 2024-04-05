# package Gun22;
#
# import java.util.ArrayList;
# import java.util.Arrays;
# import java.util.Collections;
#
# public class _01_ArrayList {
#     public static void main(String[] args) {
#         // ArrayList Collection grubunun bir elemanı
#         // Array i sıralarken Arrays.sort u kullandığımız gibi,
#         // ArrayList i Collection metodlarını kullanacağız.
#
#         ArrayList<Integer> sayilar=new ArrayList<>();
#         sayilar.add(50);
#         sayilar.add(5);
#         sayilar.add(456);
#         sayilar.add(45);
#         sayilar.add(3);
#
#         System.out.println("sayilar = " + sayilar);
#
#         //Sıralama işlemi
#         Collections.sort(sayilar);
#         System.out.println("sayilar = " + sayilar);
#
#         //Tersine çevirme
#         Collections.reverse(sayilar);
#         System.out.println("sayilar = " + sayilar);
#
#         //Max ve Min
#         System.out.println("max() = " + Collections.max(sayilar));
#         System.out.println("min() = " + Collections.min(sayilar));
#
#         //bir değer ile bütün elemanları doldurma
#         Collections.fill(sayilar, 0); // 0 değerini bütün elemanlara ver
#         System.out.println("sayilar = " + sayilar);
#
#         //istenen elemanı, istenen değerle değiştirme
#         Collections.replaceAll(sayilar, 0, 5);
#         System.out.println("sayilar = " + sayilar);
#
#         //tanımlarken değer atama
#         ArrayList<Integer> liste=new ArrayList<>( Arrays.asList(3,45,6,7,8) );
#         System.out.println("liste = " + liste);
#
#         ArrayList<String> liste2=new ArrayList<>( Arrays.asList("ismet", "mehmet", "Ayşe") );
#         System.out.println("liste2 = " + liste2);
#
#         // Bir liste çoklu eleman ekleme
#         Collections.addAll(liste, 3,4,5,6,7);  // ekleme
#         System.out.println("liste = " + liste);
#
#         // diziyi liste atmak istersek
#         Integer[] dizi2={2,3,4,5};
#         ArrayList<Integer> liste4=new ArrayList<>( Arrays.asList(dizi2) ); // direk atama
#         System.out.println("liste4 = " + liste4);
#
#     }
# }
#
#
#Bu Java kodu, ArrayList ve Collections sınıfının çeşitli metodlarını kullanarak listelerle yapılabilecek işlemleri gösteriyor:
# listeyi sıralama, ters çevirme, en büyük ve en küçük değerleri bulma, bütün elemanları belirli bir değerle doldurma,
# belirli bir değeri belirli bir değerle değiştirme, çoklu eleman ekleme ve diziyi listeye dönüştürme.
# Python'da benzer işlemleri list ve sorted(), reverse(), max(), min() gibi yerleşik fonksiyonlar kullanarak yapabiliriz:
#
#

# Liste tanımlama ve değer atama
sayilar = [50, 5, 456, 45, 3]
print("sayilar =", sayilar)

# Sıralama işlemi
sayilar.sort()
print("Sıralı sayilar =", sayilar)

# Tersine çevirme
sayilar.reverse()
print("Ters çevrilmiş sayilar =", sayilar)

# Max ve Min
print("max =", max(sayilar))
print("min =", min(sayilar))

# Bir değer ile bütün elemanları doldurma
sayilar = [0] * len(sayilar)  # 0 değerini bütün elemanlara ver
print("Sıfırlarla doldurulmuş sayilar =", sayilar)

# Tanımlarken değer atama
liste = [3, 45, 6, 7, 8]
print("liste =", liste)

liste2 = ["ismet", "mehmet", "Ayşe"]
print("liste2 =", liste2)

# Bir listeye çoklu eleman ekleme
liste.extend([3, 4, 5, 6, 7])  # Çoklu ekleme
print("Çoklu eklenmiş liste =", liste)

# Diziyi listeye atmak
dizi2 = [2, 3, 4, 5]
liste4 = list(dizi2)  # Direk atama
print("liste4 =", liste4)


#Python'da, listelerin sort() metodu ile sıralama, reverse() metodu ile ters çevirme yapılabilir.
# max() ve min() fonksiyonları liste üzerinde direkt kullanılabilir. Bir listeyi belirli bir değerle doldurmak
# için liste çarpımı ([0] * len(sayilar)) kullanılabilir. Python'da extend() metodu ile listeye çoklu eleman
# ekleme yapılabilir. Ayrıca, list() fonksiyonu ile bir dizi (veya herhangi bir iterable) listeye dönüştürülebilir.
# Bu kod, Python'daki listelerle yapılabilecek çeşitli işlemleri ve kullanışlı yöntemleri göstermektedir.