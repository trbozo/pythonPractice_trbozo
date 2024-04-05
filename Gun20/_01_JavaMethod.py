# package Gun20;
#
# public class _01_JavaMethod { //fonksiyon, Method
#     // yazılabildiği yerler
#
#     public static void main(String[] args) {
#         // amaç: main in içi sade ve okunabilir olsun,
#         // tekrarlanan kodları 1 kere yaz, istediğin kadar çalıştır Math.Random();
#         diziDoldur();
#         diziYazdir();
#         diziTeklerBul();
#
#     }
#
#     // ya da burada yazılırlar
#     public static void diziDoldur(){ // metod, fonksiyon
#         // kodlar yazılıyor
#     }
#     public static void diziYazdir(){ // metod, fonksiyon
#         // kodlar yazılıyor
#     }
#     public static void diziTeklerBul(){ // metod, fonksiyon
#         // kodlar yazılıyor
#     }
#
#
# }


# Fonksiyonlar, yazılabileceği yerler

def dizi_doldur():
    # Burada dizi doldurma ile ilgili kodlar yazılır
    pass  # Geçici olarak boş bırakmak için pass kullanıldı

def dizi_yazdir():
    # Burada dizi yazdırma ile ilgili kodlar yazılır
    pass  # Geçici olarak boş bırakmak için pass kullanıldı

def dizi_tekler_bul():
    # Burada dizi içindeki tek sayıları bulma ile ilgili kodlar yazılır
    pass  # Geçici olarak boş bırakmak için pass kullanıldı

def main():
    # Amaç: main'in içi sade ve okunabilir olsun,
    # tekrarlanan kodları 1 kere yaz, istediğin kadar çalıştır
    dizi_doldur()
    dizi_yazdir()
    dizi_tekler_bul()

# Eğer bu dosya doğrudan çalıştırılıyorsa, main fonksiyonunu çağır
if __name__ == "__main__":
    main()

##Python'da fonksiyonlar def anahtar kelimesi ile tanımlanır.
# Fonksiyonların gövdesinde yapılacak işlemler belirtilir.
# Fonksiyonlar, isimlendirilmiş ve tekrar kullanılabilir kod bloklarıdır.
# Bu kod blokları programın farklı yerlerinden çağrılarak kullanılabilir.
# main() fonksiyonu, programın ana giriş noktası olarak kullanılır ve diğer fonksiyonları çağırır.
# Bu yapı, kodun daha düzenli ve okunabilir olmasını sağlar.
