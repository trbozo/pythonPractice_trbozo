# // package Gun10;
# //
# // import java.util.Scanner;
# //
# // public class _03_JavaIf {
# //     public static void main(String[] args) {
# //         // Girilen bir cümlede a harfinin geçip geçmediğini
# //         // bulunuz geçiyor ise EVET, geçmiyor ise HAYIR yazdırınız
# //
# //         Scanner oku=new Scanner(System.in);
# //         System.out.print("Cumle giriniz= ");
# //         String cumle=oku.nextLine();
# //
# //         // 1.Yöntem
# //         boolean varMi= cumle.contains("a");
# //
# //         if (varMi == true)
# //             System.out.println("EVET");
# //
# //         if (varMi == false)
# //             System.out.println("HAYIR");
# //
# //         //2.Yöntem
# //         if (cumle.contains("a") == true)
# //             System.out.println("EVET");
# //
# //         if (cumle.contains("a") == false)
# //             System.out.println("HAYIR");
# //
# //         //3.Yöntem
# //         boolean varMi2= cumle.contains("a");
# //
# //         if (varMi2)     // varMi==true  varMi
# //             System.out.println("EVET");
# //
# //         if (!varMi2)
# //             System.out.println("HAYIR");
# //
# //
# //         //4.Yöntem
# //         if (cumle.contains("a"))
# //             System.out.println("EVET");
# //
# //         if (!cumle.contains("a"))
# //             System.out.println("HAYIR");
# //
# //     }
# // }

cumle = input("Cumle giriniz= ")

# 1.Yöntem
var_mi = "a" in cumle

if var_mi:
    print("EVET")
else:
    print("HAYIR")

# 2.Yöntem ve 3.Yöntem Python'da bu şekilde optimize edilebilir.

# 4.Yöntem
if "a" in cumle:
    print("EVET")
else:
    print("HAYIR")

#Python'da bir string içinde bir karakterin veya bir alt string'in var olup olmadığını kontrol etmek için
# "a" in cumle ifadesi kullanılır. Bu, Java'nın cumle.contains("a") metoduna eşdeğerdir.
# if koşulu Python'da doğrudan bu ifade ile kullanılabilir ve == true ya da == false kullanımına gerek yoktur.
# Bu kod, girilen bir cümlede 'a' harfinin geçip geçmediğini kontrol eder ve sonuç olarak "EVET" veya "HAYIR" mesajını yazdırır.