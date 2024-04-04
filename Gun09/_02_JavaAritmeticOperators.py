#// package Gun09;
#//
#// public class _02_JavaAritmeticOperators {
#//     public static void main(String[] args) {
##//         int toplam = 0, sayi = 1;
#//
#//         toplam = toplam + sayi;   // toplama sayıyı ekle : 1 oldu toplam
#//         sayi = sayi + 1;          // sayi yi 1 artır
#//
#//         // bu 2 satırı tek satırda yazabilirsin diyor
#//         toplam=0; sayi=1; // başlangıç değerlerine getirildi
#//
##//         toplam = toplam + sayi++; // toplam =1, sayi =2
#//         // ++ sadece sayıyı etkiler
#//
#//         /*********************************************/
#//         toplam=0; sayi=1; // başlangıç değerlerine getirildi
#//
#//         sayi=sayi+1;
#//         toplam=toplam+sayi;         // sayi=2,  toplam=2
#//
#//         //bu iki satır yerine tek satırda şöyle yazabilirsin
#//         toplam=0; sayi=1; // başlangıç değerlerine getirildi
#//
#//         toplam = toplam +  ++sayi;   // sayi=2,  toplam=2
#//
#//         //  ++ sonra ise, önce işlem, sonra artış
#//         //  ++ önce ise, önce artış,  sonra işlem
#//     }
#// }


# İlk örnek
toplam = 0
sayi = 1

toplam += sayi  # toplama sayıyı ekle: 1 oldu toplam
sayi += 1       # sayiyi 1 artır

# Bu 2 satırı tek satırda şöyle yazabilirsiniz:
toplam, sayi = 0, 1  # Başlangıç değerlerine getirildi

toplam += sayi
sayi += 1            # toplam=1, sayi=2 artık

# İkinci örnek
toplam, sayi = 0, 1  # Başlangıç değerlerine getirildi

sayi += 1
toplam += sayi       # sayi=2, toplam=2

# Bu iki satır yerine tek satırda şöyle yazabilirsiniz:
toplam, sayi = 0, 1  # Başlangıç değerlerine getirildi

sayi += 1
toplam += sayi       # sayi=2, toplam=2

print("Toplam:", toplam, "Sayi:", sayi)

##Python'da ++ ve -- operatörleri olmadığı için, sayi += 1 veya sayi -= 1 şeklinde yazılır.
# Bu kod, sayi değişkenini artırdıktan sonra toplam değişkenine sayi'nin değerini eklemeyi göstermektedir.
# Python'da işlemler soldan sağa doğru gerçekleşir, bu yüzden sayi++ ya da ++sayi yerine doğrudan sayi += 1 kullanılır.
# Bu örnekte, aynı sonuçları elde etmek için Python dilindeki eşdeğer yaklaşımı kullandık.