# package Gun11;
#
# import java.util.Scanner;
#
# public class _01_IfElse {
#     public static void main(String[] args) {
#         // Girilen bir stringin uzunluğu 10 dan büyükse ve string içinde
#         // "study" kelimesi(büyük veya küçük) geçiyorsa ekrana evet
#         // yazdırın değilse  hayır yazdırınız.
#
#         Scanner oku=new Scanner(System.in);
#         System.out.print("Cümle giriniz=");
#         String cumle=oku.nextLine();
#
# //        Eğer cumle 10 karakterden büyükse VE içinde study kelimesi geçiyorsa
# //               EVET yaz
# //        Değilse
# //               HAYIR yaz
#
#         // 1.Yöntem
#           if ( cumle.length() > 10 && cumle.toLowerCase().contains("study") )
#               System.out.println("EVET");
#           else
#               System.out.println("HAYIR");
#
#           // 2.Yöntem
#         int uzunluk=cumle.length();
#         boolean varMi= cumle.toLowerCase().contains("study");
#
#         if (uzunluk > 10 && varMi)
#             System.out.println("EVET");
#         else
#             System.out.println("HAYIR");
#
#     }
# }


cumle = input("Cümle giriniz=")

# 1.Yöntem
if len(cumle) > 10 and "study" in cumle.lower():
    print("EVET")
else:
    print("HAYIR")

# 2.Yöntem
uzunluk = len(cumle)
var_mi = "study" in cumle.lower()

if uzunluk > 10 and var_mi:
    print("EVET")
else:
    print("HAYIR")


#kullanıcıdan bir cümle alır ve bu cümlenin uzunluğunun 10 karakterden büyük olup olmadığını ve içinde "study" kelimesinin (büyük veya küçük harf fark etmeksizin) geçip geçmediğini kontrol eder. Şartlar sağlanıyorsa "EVET", aksi halde "HAYIR" yazdırır. Python'da len() fonksiyonu stringin uzunluğunu verirken, .lower() metodu stringi küçük harfe dönüştürür ve "kelime" in cumle yapısıyla kelimenin cümle içinde geçip geçmediği kontrol edilir.