# package Gun17;
#
# import java.util.Arrays;
#
# public class _05_JavaArrayMetodlar {
#     public static void main(String[] args) {
#         String[] isimler={"Ahmet","Zeynep","Roman","Cihan"};
#
#         //diiyi ekrana direk yazdırmak
#         System.out.println("isimler = " + Arrays.toString(isimler));
#
#         //dizi sıralama
#         Arrays.sort(isimler);
#         System.out.println("isimler = " + Arrays.toString(isimler));
#
#         int[] a={1,8,65,45};
#         Arrays.sort(a);
#         System.out.println("en küçük = " + a[0]);
#         System.out.println("en büyük = " + a[a.length-1]);
#
#         // Elemanları hızlı doldurma aynı değerle
#         Arrays.fill(a,5);//hepsine 5 doldur
#         System.out.println("a = " + Arrays.toString(a));
#     }
# }

isimler = ["Ahmet", "Zeynep", "Roman", "Cihan"]
print("isimler =", isimler)

isimler.sort()
print("isimler =", isimler)

a = [1, 8, 65, 45]
a.sort()
print("en küçük =", a[0])
print("en büyük =", a[-1])

a = [5] * len(a)
print("a =", a)


#Bu Python kodu, sort() yöntemini kullanarak dizileri sıralar, len() işlevini kullanarak bir dizinin uzunluğunu alır ve * operatörünü kullanarak bir diziyi belirli bir değerle doldurur.






