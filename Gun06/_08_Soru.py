# package Gun06;
#
# import java.util.Scanner;
#
# public class _08_Soru {
#     public static void main(String[] args) {
#         // Girilen bir stringin sadece son Harfini yazdırınız.
#
#         Scanner oku=new Scanner(System.in);
#         System.out.print("Cümle giriniz=");
#         String cumle=oku.nextLine();
#
#         int uzunluk = cumle.length();
#         char sonHarf= cumle.charAt(uzunluk-1); // SON HARF
#         System.out.println("sonHarf = " + sonHarf);
#     }
# }


# Java kodunun Python'a dönüştürülmüş hali

# Girilen bir stringin sadece son Harfini yazdırınız.

cumle = input("Cümle giriniz=")

uzunluk = len(cumle)
sonHarf = cumle[uzunluk - 1]  # SON HARF
print("sonHarf =", sonHarf)


#Bu Python kodu, kullanıcıdan bir cümle alır ve cümlenin son harfini yazdırır. Python'da, bir stringin son karakterine erişmek için negatif indeksleme kullanılabilir. Bu durumda, -1 indeksi en son karakteri, -2 indeksi sondan bir önceki karakteri vb. ifade eder.






