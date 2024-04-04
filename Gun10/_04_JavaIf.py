# // package Gun10;
# //
# // import java.util.Scanner;
# //
# // public class _04_JavaIf {
# //     public static void main(String[] args) {
# //         // Girilen bir cümledeki küçük veya büyük a harfinin olup olmadığı yazdırınız
# //         // VAR veya YOK şeklinde
# //
# // //        hava  -> var desin
# // //        HAVA  -> var desin
# //
# //         Scanner oku= new Scanner(System.in);
# //         System.out.print("Cümle giriniz=");
# //         String cumle=oku.nextLine();
# //
# //         cumle = cumle.toUpperCase();
# //
# //         if (cumle.contains("A"))
# //             System.out.println("VAR");
# //
# //         if (!cumle.contains("A"))
# //             System.out.println("YOK");
# //
# //
# //         /********* farklı yontem  ******************/
# //
# //         String aSizCumle = cumle.replace("A","").replace("a","");
# //         //String aSizCumle = cumle.replaceAll("[aA]","");
# //
# //         if (aSizCumle.length() == cumle.length())
# //             System.out.println("YOK");
# //
# //         if (aSizCumle.length() != cumle.length())
# //             System.out.println("VAR");
# //
# //
# //     }
# // }


cumle = input("Cümle giriniz=")

cumle = cumle.upper()

if "A" in cumle:
    print("VAR")
else:
    print("YOK")

# Farklı yöntem
a_siz_cumle = cumle.replace("A", "").replace("a", "")  # Python'da upper() uygulandığı için "a" yerine "A" kontrolü yeterli olur.

if len(a_siz_cumle) == len(cumle):
    print("YOK")
else:
    print("VAR")


##Bu Python kodu, girilen bir cümledeki küçük veya büyük 'a' harfinin olup olmadığını kontrol eder
# ve "VAR" veya "YOK" şeklinde sonuç yazdırır. İlk yöntemde, girilen cümleyi büyük harfe çevirerek
# tüm harfleri büyütür ve ardından 'A' harfinin olup olmadığını kontrol eder. İkinci yöntemde, cümleden
# 'A' harflerini çıkarır ve orijinal cümle ile uzunluğu karşılaştırarak 'A' harfinin olup olmadığını kontrol eder.
# Bu yöntemler, Java'daki kodun mantığını yansıtmaktadır.