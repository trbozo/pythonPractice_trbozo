# package Gun22;
#
# import java.util.ArrayList;
# import java.util.Scanner;
#
# public class _03_Soru {
#     public static void main(String[] args) {
#         // Bir canlı sözlük yapılmak isteniyor,
#         // Kullanıcıdan kelime ve manası şeklinde
#         // Devam ietmek istediği kadar bilgi alınız
#         // 2 bilgi alınız.
#         // Daha sonra kullanıcıdan bir kelime alarak
#         // manasını yazdırınız.
#
#         // kelimeler bi yerde , anlamları bi yerde olacak
#         ArrayList<String> kelimeler=new ArrayList<>();
#         ArrayList<String> manalari=new ArrayList<>();
#
#         ArrayList< ArrayList<String> > sozluk=new ArrayList<>();
#         sozluk.add(kelimeler);
#         sozluk.add(manalari);
#
#         Scanner okuStr=new Scanner(System.in);
#
#         String cevap="";
#         do{
#             System.out.print("Kelime giriniz=");
#             String kelime= okuStr.nextLine();
#             kelimeler.add(kelime);  //sozluk.get(0).add(kelime);
#
#             System.out.print("Manasını giriniz=");
#             String mana= okuStr.nextLine();
#             manalari.add(mana); //sozluk.get(1).add(kelime);
#
#             System.out.print("Devam etmek istiyor musunuz?(E/H)=");
#             cevap= okuStr.nextLine();
#
#         }while(cevap.equalsIgnoreCase("E"));
#
#         System.out.print("Aranacak Kelime=");
#         String arananKelime= okuStr.nextLine();
#
#         // şimdi arana kelimeyi bulalım
#         for (int i = 0; i < kelimeler.size(); i++) {  // sozluk.get(0).size()
#             if (kelimeler.get(i).equalsIgnoreCase(arananKelime)) //kelime bulundu
#             {
#                 System.out.println(manalari.get(i));
#             }
#         }
#
#     }
# }
#
#Bu Java kodu, basit bir sözlük uygulaması yapısını gösterir.
# Kullanıcıdan alınan kelimeler ve manaları iki ayrı ArrayList'te saklar ve daha sonra bir kelime arandığında onun
# manasını gösterir. Python'da, bu işlemi bir dict (sözlük) yapısı kullanarak daha verimli bir şekilde gerçekleştirebiliriz.
# Python'daki dict,
# anahtar-değer çiftlerini saklamak için idealdir ve bu durumda kelime ve manaları ilişkilendirmek için kullanılabilir:
#
#Python'da Sözlük Kullanarak Kelime-Mana Eşleştirmesi


def main():
    sozluk = {}  # Kelimeler ve manaları saklamak için boş bir sözlük oluşturulur

    while True:
        # Kullanıcıdan kelime ve manasını alma
        kelime = input("Kelime giriniz: ")
        mana = input("Manasını giriniz: ")

        # Sözlüğe kelime ve manasını ekleme
        sozluk[kelime] = mana

        # Kullanıcıdan devam edip etmek istemediğini sorma
        cevap = input("Devam etmek istiyor musunuz? (E/H): ")
        if cevap.upper() == "H":
            break  # Kullanıcı 'H' cevabı verirse döngüden çıkılır

    # Kullanıcıdan aranacak kelimeyi alma
    aranan_kelime = input("Aranacak Kelime: ")

    # Aranan kelimenin manasını yazdırma
    mana = sozluk.get(aranan_kelime)  # get() metodu, kelime sözlükte yoksa None döner
    if mana:
        print(f"{aranan_kelime} kelimesinin manası: {mana}")
    else:
        print(f"{aranan_kelime} kelimesi sözlükte bulunamadı.")

if __name__ == "__main__":
    main()

##Bu kod, kelimeleri ve manalarını bir sözlükte (dict) saklar.
# Kullanıcı H harfi girip programdan çıkmak isteyinceye kadar kelime ve manalarını girmeye devam edebilir.
# Daha sonra kullanıcıdan bir kelime alınır ve bu kelimenin manası, eğer sözlükte varsa, ekrana yazdırılır.
# Python'daki sözlük yapısı (dict),
# bu tür anahtar-değer eşleştirmeleri için çok uygundur ve veri erişimi açısından oldukça hızlıdır.
