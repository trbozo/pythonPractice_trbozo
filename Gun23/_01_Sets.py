# package Gun23;
#
# import java.util.ArrayList;
#
# public class _01_Sets {
#     public static void main(String[] args) {
#         int sayi=5;
#
#         int[] dizi=new int[10]; //1D
#         int[][] tablo=new int[2][5]; //2D
#
#         ArrayList<Integer> liste=new ArrayList<>(); //1D
#         ArrayList< ArrayList<Integer> > listeler=new ArrayList<>(); //2D
#
#         /********************************************************/
#
#         // Java cım sendne şu ana kadar lazım durumda uygun değişkenleri aldım, teşekkür ederim.
#         // fakat bana şöyle dizi lazım; içine verileri attığımda tekrar eden veri gelirse EKLEMESİN,
#         // 2.cisi, bu dizi
#         // a) istersem, ne eklersem ekliyim, herzaman içindekileri SIRALI tutsun,
#         // b) istersem, eklenmese sırasında tutsun
#         // c) istersem, en hızlı çalışmak için, kendisi istediği sırada tutsun
#
#         // tek tek eleman eleman işlemler için değilde, işlem yapılacağı zaman, bütün elemanla işleme
#         // alınmasına uygun olan bu toplu işlem dizisine SET denir.
#         // a) TreeSet -> herzaman sıralı
#         // b) LinkedHashSet -> eklenme sırasına göre
#         // c) HashSet -> hızlı çalışsın sırası önemli değil
#
#         // Bunlarda INDEX yok
#
#
#
#
#
#
#
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


# #Python'da, Java'nın Set koleksiyonlarına benzer yapılar için set ve frozenset kullanılır.
# Python'daki set, elemanları sırasız bir şekilde saklar ve tekrar eden elemanlara izin vermez.
# Ancak, setler değiştirilebilir (mutable) olduğundan, içerikleri çalışma zamanında değiştirilebilir.
# frozenset, setin değiştirilemez (immutable) versiyonudur ve içeriği tanımlandıktan sonra değiştirilemez.
#
# Python'da setler, hem hızlı çalışır hem de tekrar eden elemanları otomatik olarak filtreler.
# Ancak, setlerde elemanların eklenme sırası korunmaz. Eğer eklenme sırasının korunması isteniyorsa,
# Python 3.6 ve sonrasında normal set kullanılarak bu sağlanabilir çünkü Python 3.6'dan itibaren setler eklenme
# sırasını koruma özelliğine sahip oldu. Ancak, bu davranış resmi olarak belgelenmemiş bir uygulama detayı olduğundan,
# sıralı bir yapıya ihtiyaç duyulduğunda collections.OrderedDict veya Python 3.7 ve üzeri için dict kullanılabilir.
# dictler de Python 3.7'den itibaren eklenme sırasını koruma garantisi vermektedir.
#
# TreeSet gibi sıralı bir yapıya ihtiyaç duyulduğunda Python'da doğrudan bir karşılığı yoktur,
# ancak bu davranış sorted() fonksiyonu kullanılarak elde edilebilir veya blist gibi üçüncü parti
# kütüphanelerden yararlanılabilir.


# Set oluşturma ve kullanma
my_set = {3, 1, 4, 2, 2}
print(my_set)  # Çıktı: {1, 2, 3, 4}

# Sıralı bir set için
my_sorted_set = sorted(my_set)
print(my_sorted_set)  # Çıktı: [1, 2, 3, 4]

# Frozenset kullanımı
my_frozenset = frozenset([3, 1, 4, 2, 2])
print(my_frozenset)  # Çıktı: frozenset({1, 2, 3, 4})


#Bu örneklerde görüldüğü gibi, Python'da set kullanımı oldukça basittir ve tekrar eden
# elemanları otomatik olarak kaldırır. Sıralama ihtiyacı için sorted() fonksiyonu kullanılabilir.
# frozenset ise değiştirilemez bir set oluşturmak için kullanılır.