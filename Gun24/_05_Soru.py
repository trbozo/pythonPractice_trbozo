# package Gun24;
#
# import java.util.HashMap;
# import java.util.Scanner;
#
# public class _05_Soru {
#     public static void main(String[] args) {
#         // Canlı Sözlük yapılmak isteniyor.
#         // Kullanıcıya aşağıdaki gibi bir menü çıkarınız.
#         // 1- Ekleme (Bu secekte kelimenin kendisi alınız ve manasını alınız)
#         // 2- Düzeltme (Bu secenkte kullanıcının kelimenin manasını düzelttiriniz.)
#         // 3- Listeleme
#         // 4- Arama (Bu secekte verilen bir kelime nin manasını yazıdırnız)
#         // 5- Silme
#         // 6- Çıkış
#
#         // kelime ve manası , kelimeden de manaya ulaşabilmm lazım
#         Scanner okuInt = new Scanner(System.in);
#         Scanner okuStr = new Scanner(System.in);
#         HashMap<String, String> sozluk=new HashMap<>();
#         int secim=0;
#         do{
#             // kullanıcyya menüyü göster
#             System.out.print("MENÜ\n1-EKLEME\n2-DÜZLETME\n3-LİSTELEME" +
#                     "\n4-ARAMA\n5-SİLME\n6-ÇIKIŞ\nSeçiminiz=");
#             secim=okuInt.nextInt();
#             // seçimini al
#             // seçime göre işlemi yap
#             switch (secim){
#                 case 1: // ekleme işlemleri
#                     System.out.print("Kelime giriniz=");
#                     String kelime= okuStr.nextLine();
#                     System.out.print("Anlamı=");
#                     String anlami= okuStr.nextLine();
#                     sozluk.put(kelime, anlami);
#                     System.out.println("Ekleme işlemi yapılmıştır");
#                     break;
#                 case 2: //düzeltme işlemleri ;
#                     break;
#                 case 3: //listeleme işlemleri ;
#                     break;
#                 case 4: //arama işlemleri ;
#                     System.out.print("Aranan Kelime giriniz=");
#                     kelime= okuStr.nextLine();
#                     System.out.println(sozluk.get(kelime));
#                     break;
#                 case 5: //silme işlemleri ;
#                     break;
#             }
#
#         }while(secim !=6);
#
#
#
#     }
# }

def main():
    sozluk = {}
    while True:
        # Kullanıcıya menüyü göster
        print("""
        MENÜ
        1- EKLEME
        2- DÜZELTME
        3- LİSTELEME
        4- ARAMA
        5- SİLME
        6- ÇIKIŞ
        """)
        secim = int(input("Seçiminiz: "))

        if secim == 1:  # Ekleme işlemleri
            kelime = input("Kelime giriniz: ")
            anlami = input("Anlamı: ")
            sozluk[kelime] = anlami
            print("Ekleme işlemi yapılmıştır.")

        elif secim == 2:  # Düzeltme işlemleri
            kelime = input("Düzeltilecek kelimeyi giriniz: ")
            if kelime in sozluk:
                yeni_anlam = input("Yeni anlamını giriniz: ")
                sozluk[kelime] = yeni_anlam
                print("Düzeltme işlemi yapılmıştır.")
            else:
                print("Sözlükte bu kelime bulunamadı.")

        elif secim == 3:  # Listeleme işlemleri
            for k, v in sozluk.items():
                print(f"{k}: {v}")

        elif secim == 4:  # Arama işlemleri
            kelime = input("Aranan kelimeyi giriniz: ")
            if kelime in sozluk:
                print(sozluk[kelime])
            else:
                print("Bu kelime sözlükte bulunamadı.")

        elif secim == 5:  # Silme işlemleri
            kelime = input("Silinecek kelimeyi giriniz: ")
            if kelime in sozluk:
                del sozluk[kelime]
                print("Silme işlemi yapılmıştır.")
            else:
                print("Sözlükte bu kelime bulunamadı.")

        elif secim == 6:  # Çıkış işlemi
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyiniz.")


if __name__ == "__main__":
    main()

