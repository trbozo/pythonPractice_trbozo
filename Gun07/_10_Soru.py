# package Gun07;
#
# import java.util.Scanner;
#
# public class _10_Soru {
#     public static void main(String[] args) {
#         // Tek seferde girilen bir ad soyadın(tam ad) adını ve soyadını ayırıp,
#         // ayrı ayrı yazdırınız. (sadece ad ve soyad)
#         // mesala İsmet Temur -> İsmet i ayrı yazdırın, Temur u yazdırın
#
#         Scanner oku=new Scanner(System.in);
#
#         System.out.print("Ad ve Soyad= ");
#         String adSoyad= oku.nextLine();
#
#         int boslukIndex = adSoyad.indexOf(" ");
#
#         String ad = adSoyad.substring(0, boslukIndex);
#         String soyad = adSoyad.substring(boslukIndex+1);
#
#         System.out.println("ad = " + ad);
#         System.out.println("soyad = " + soyad);
#     }
# }


# Java kodunun Python'a dönüştürülmüş hali

# Tek seferde girilen bir ad soyadın(tam ad) adını ve soyadını ayırıp,
# ayrı ayrı yazdırınız. (sadece ad ve soyad)
# mesala İsmet Temur -> İsmet i ayrı yazdırın, Temur u yazdırın

ad_soyad = input("Ad ve Soyad= ")

bosluk_index = ad_soyad.index(" ")

ad = ad_soyad[:bosluk_index]
soyad = ad_soyad[bosluk_index + 1:]

print("ad =", ad)
print("soyad =", soyad)


#Bu Python kodu, kullanıcıdan alınan tam adı ayırarak ad ve soyadını ayrı ayrı yazdırır. Python'da, index metodu kullanılarak boşluk karakterinin indexi bulunur. Ardından, dilimleme (slicing) yöntemiyle ad ve soyad ayrı ayrı elde edilir.






