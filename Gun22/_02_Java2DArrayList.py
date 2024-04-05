# package Gun22;
#
# import java.util.ArrayList;
#
# public class _02_Java2DArrayList {
#     public static void main(String[] args) {
#         int sayi=5; // tek bir rakam saklayabilen değişken.
#         int[] dizi=new int[10]; // 10 elemanlı tek boyutlu bir hafıza bölgesi 1D
#         int[][] tablo=new int[2][5]; // 10 eleman ama 2 satır halinde 2D
#
#         ArrayList<Integer> liste=new ArrayList<>(); // tek satır 1D, ucu açık
#
#         // bir öğretmenin notDefteri olsun
#         ArrayList<Integer> matNotlari=new ArrayList<>(); // ayrı yaprak, liste, 1D
#         ArrayList<Integer> fizNotlari=new ArrayList<>(); // ayrı yaprak, liste, 1D
#         ArrayList<Integer> kimNotlari=new ArrayList<>(); // ayrı yaprak, liste, 1D
#
#         matNotlari.add(50);
#         matNotlari.add(70);
#         matNotlari.add(80);
#
#         fizNotlari.add(40);
#         fizNotlari.add(60);
#
#         kimNotlari.add(90);
#         kimNotlari.add(50);
#         kimNotlari.add(60);
#         kimNotlari.add(87);
#
#         /******************************/
#         ArrayList<  ArrayList<Integer>  >  notlarListesi = new ArrayList<>();
#         notlarListesi.add(matNotlari);
#         notlarListesi.add(fizNotlari);
#         notlarListesi.add(kimNotlari);
#
#         matNotlari.get(0);  // mat notlarının ilkini verir.
#         notlarListesi.get(0).get(0); // 0.listenin, 0.elemanı , aynı satır sütun gibi.
#         // defterin.  0.Sayfasının.   0.Elemanı
#         // notlarListesi.get(0)  -> ilk eklenen listeyi verir
#         notlarListesi.get(0).add(67);  // matNotlarına 1 eleman daha eklendi
#
#         for (int i = 0; i < notlarListesi.size() ; i++) { // notlar.length
#
#             for (int j = 0; j < notlarListesi.get(i).size(); j++) {  //notlar[i].length
#                 System.out.print(notlarListesi.get(i).get(j)+"\t"); // notlar[i][j]
#             }
#
#             System.out.println();
#         }
#
#
#
#     }
# }
#
#Bu Java kodu, farklı dersler için öğrenci notlarını tutan 2 boyutlu bir ArrayList yapısını gösteriyor.
# ArrayList içinde ArrayList tutarak çok boyutlu dinamik yapılar oluşturulabilir.
# Python'da, listelerin esnek yapısını kullanarak benzer bir yapıyı kolayca oluşturabiliriz:
#
#Python'da 2D List (Liste İçinde Liste) Kullanımı

def main():
    # Tek bir rakam saklayabilen değişken.
    sayi = 5

    # 10 elemanlı tek boyutlu bir hafıza bölgesi 1D
    dizi = [0] * 10

    # 10 eleman ama 2 satır halinde 2D
    tablo = [[0 for _ in range(5)] for _ in range(2)]

    # Tek satır 1D, ucu açık
    liste = []

    # Bir öğretmenin not defteri olsun
    mat_notlari = [50, 70, 80]
    fiz_notlari = [40, 60]
    kim_notlari = [90, 50, 60, 87]

    # Notlar listesini oluşturma
    notlar_listesi = [mat_notlari, fiz_notlari, kim_notlari]

    # Mat notlarının ilkini verir
    print(mat_notlari[0])

    # 0. listenin 0. elemanı, aynı satır sütun gibi
    print(notlar_listesi[0][0])

    # Mat notlarına bir eleman daha eklenir
    notlar_listesi[0].append(67)

    # Notların yazdırılması
    for ders_notlari in notlar_listesi:
        for notu in ders_notlari:
            print(notu, end="\t")
        print()


if __name__ == "__main__":
    main()





