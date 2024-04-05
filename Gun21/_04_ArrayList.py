# package Gun21;
#
# import java.util.ArrayList;
#
# public class _04_ArrayList {
#     public static void main(String[] args) {
#         int sayi=5;  // 1 tane sayı tutabilen ve ismi syai hafıza bölgesi
#         int[] dizi=new int[5];  // 5 tane sayı tutabilen ve ismi dizi olan hafıza bölgesi(apartman)
#         // 5 tane 5 kalıyor, 3 tane kullansan 2 tanesi atıl kalıyor, uzunluk hep sabit
#         // ARRAY
#
#         //dizinin yerine şöyle bir şey olsa, uzunluğu başta hiç olmasa, ben ekledikçe artsa
#         // sildikçe azalsa , yani alışveriş listesi gibi, boyutu esnek olsun
#         // dizini kuzeni : ARRAY in LİST hali
#
#         ArrayList<Integer> list=new ArrayList<>(); // ekledikçe uzayacak, sildikçe kısalacak
#         ArrayList<String> stringList=new ArrayList<>();
#         ArrayList<Double> doubleList=new ArrayList<>();
#
#         ArrayList<String> isimler=new ArrayList<>();
#         System.out.println("isimler = " + isimler);//direk fotoğraf
#
#         isimler.add("Burak"); // eleman ekleme
#         isimler.add("Aslı");
#         isimler.add("Selda");
#         isimler.add("Serkan");
#
#         System.out.println("isimler = " + isimler);
#         System.out.println("isimler.size() = " + isimler.size());
#
#         isimler.add(1, "Mertcan"); // araya ekleme, diğerleri bir üste kayar
#         System.out.println("isimler = " + isimler);
#
#         isimler.set(2,"Ulvi");  // verilen indexdeli, elemanı değiştirmek
#         System.out.println("isimler = " + isimler);
#
#         boolean varMi= isimler.contains("Burak");
#         System.out.println("varMi = " + varMi);
#
#         isimler.remove(1); // rakam verildiğinde index olarak görür ve siler
#         System.out.println("isimler = " + isimler);
#
#         int indexOfSelda=isimler.indexOf("Selda"); // verilenin indexi ni gönderir
#         System.out.println("indexOfSelda = " + indexOfSelda);
#
#         String ilkEleman= isimler.get(0); // verilen indexdeki elemanı verir
#         System.out.println("ilkEleman = " + ilkEleman);
#
#         isimler.clear(); // Listi temizler
#         System.out.println("isimler = " + isimler);
#
#
#     }
# }

##Python'da List Kullanımı

# Listeler Python'da ArrayList'in karşılığıdır ve dinamik olarak boyutlandırılabilir.

isimler = []  # Boş bir liste oluşturuluyor
print("isimler =", isimler)

# Eleman ekleme
isimler.append("Burak")
isimler.append("Aslı")
isimler.append("Selda")
isimler.append("Serkan")
print("isimler =", isimler)
print("isimlerin boyutu =", len(isimler))

# Araya eleman ekleme
isimler.insert(1, "Mertcan")  # 1. indexe "Mertcan" eklenir
print("isimler =", isimler)

# Belirli bir indexdeki elemanı değiştirme
isimler[2] = "Ulvi"  # 2. indexdeki eleman "Ulvi" ile değiştirilir
print("isimler =", isimler)

# Bir elemanın listede olup olmadığını kontrol etme
var_mi = "Burak" in isimler
print("var_mi =", var_mi)

# Belirli bir indexteki elemanı silme
del isimler[1]  # 1. indexdeki eleman silinir
print("isimler =", isimler)

# Bir elemanın indexini bulma
index_of_selda = isimler.index("Selda")  # "Selda"nın indexi bulunur
print("index_of_selda =", index_of_selda)

# Belirli bir indexteki elemanı alma
ilk_eleman = isimler[0]  # 0. indexdeki eleman alınır
print("ilk_eleman =", ilk_eleman)

# Listenin tamamını temizleme
isimler.clear()
print("isimler =", isimler)


##Python listeleri, ArrayList gibi dinamik bir yapı sunar ve boyutları ihtiyaca göre otomatik olarak ayarlanır.
# Listeler üzerinde yapılan işlemler, append(), insert(), del, index(), clear() gibi metodlar ve
# işlemler ile kolaylıkla gerçekleştirilebilir.
# Bu kod parçası, Python'daki listelerin nasıl kullanılacağını ve çeşitli işlemlerin nasıl yapılabileceğini göstermektedir.

