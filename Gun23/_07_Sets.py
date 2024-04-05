# package Gun23;
#
# import java.util.HashSet;
#
# public class _07_Sets {
#     public static void main(String[] args) {
#         HashSet<Integer> setA=new HashSet<>();
#         setA.add(1);
#         setA.add(2);
#         setA.add(3);
#         setA.add(4);
#         setA.add(5);
#
#         HashSet<Integer> setB=new HashSet<>();
#         setB.add(4);
#         setB.add(5);
#         setB.add(6);
#         setB.add(7);
#
#         System.out.println("setA = " + setA);
#         System.out.println("setB = " + setB);
#
#         // birleştirme
#         HashSet<Integer> birlesikHali=new HashSet<>();
#         birlesikHali.addAll(setA);
#         birlesikHali.addAll(setB);
#         System.out.println("birlesikHali = " + birlesikHali);
#
#         //farkını bulma
#         HashSet<Integer> farki=new HashSet<>();
#         farki.addAll(setA);
#         farki.removeAll(setB);
#         System.out.println("farki = " + farki);
#
#         //kesişim bulma
#         HashSet<Integer> ortakElemanlar=new HashSet<>();
#         ortakElemanlar.addAll(setA);
#         ortakElemanlar.retainAll(setB);
#         System.out.println("ortakElemanlar = " + ortakElemanlar);
#
#
#
#
#
#
#     }
# }

# Bu Java kodu, iki HashSet koleksiyonu arasındaki birleşim, fark ve kesişim işlemlerini gerçekleştirir.
# İki farklı HashSet (setA ve setB) tanımlanır ve her birine bazı elemanlar eklenir. Ardından bu iki set
# arasındaki birleşim, fark ve kesişim işlemleri için aşağıdaki yöntemler kullanılır:
#
# Birleşim (addAll metodu): İki setin tüm elemanlarını içeren yeni bir set oluşturur.
# Tekrar eden elemanlar yalnızca bir kez yer alır.
#
# Fark (removeAll metodu): setA'dan, setB'de bulunan elemanları çıkararak setA'nın setB'ye göre farkını hesaplar.
#
# Kesişim (retainAll metodu): setA ve setB'nin ortak elemanlarını içeren bir set oluşturur.
#
# Python'da bu işlemleri set yapısı kullanarak benzer şekilde gerçekleştirebiliriz.
# Python'daki setler de tekrar eden elemanlara izin vermez ve matematiksel küme işlemleri için uygun metodlara sahiptir:
#
# Python'da Set İşlemleri


setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7}

print("setA =", setA)
print("setB =", setB)

# Birleşim
birlesik_hali = setA.union(setB)
print("Birleşik Hali =", birlesik_hali)

# Fark
farki = setA.difference(setB)
print("Farkı =", farki)

# Kesişim
ortak_elemanlar = setA.intersection(setB)
print("Ortak Elemanlar =", ortak_elemanlar)


# Bu Python kodu, union, difference ve intersection metodlarını kullanarak iki set arasındaki birleşim,
# fark ve kesişim işlemlerini gerçekleştirir. Sonuçlar, Java'daki işlemlere paralel olarak elde edilir.
# Bu, setlerin hem Java hem de Python'da benzer şekilde kullanılabileceğini gösterir.