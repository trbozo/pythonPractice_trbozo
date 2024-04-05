# package Gun23;
#
# import java.util.Arrays;
# import java.util.Collections;
# import java.util.TreeSet;
#
# public class _06_Soru {
#     public static void main(String[] args) {
#         // 10 elamanlı bir diziyi random(10(dahil) a kadar olan sayılarla
#         // doldurduktan, tekrarlı değerleri almayacak şekilde yeni bir
#         // diziye atınız.
#
#         Integer[] dizi=new Integer[10];
#
#         for (int i = 0; i < dizi.length; i++)
#             dizi[i]= (int)(Math.random()*11);
#
#         System.out.println("dizi = " + Arrays.toString(dizi));
#
#         //1.Yöntem
#         TreeSet<Integer> ts=new TreeSet<>();
#         for (int i = 0; i < dizi.length; i++)
#               ts.add( dizi[i] ) ;
#
#         System.out.println("ts = " + ts);
#
#         //2.Yöntem
#         TreeSet<Integer> ts2=new TreeSet<>( Arrays.asList(dizi) );
#         System.out.println("ts2 = " + ts2);
#
#         //3.Yöntem
#         TreeSet<Integer> ts3=new TreeSet<>();
#         ts3.addAll( Arrays.asList(dizi) );
#         System.out.println("ts3 = " + ts3);
#
#         //4.Yöntem
#         TreeSet<Integer> ts4=new TreeSet<>();
#         Collections.addAll(ts4, dizi);
#         System.out.println("ts4 = " + ts4);
#     }
# }


# #Bu Java kodu, TreeSet kullanarak 10 elemanlı bir diziyi, 0'dan 10'a kadar rastgele sayılarla doldurur ve
# tekrarlanan değerleri hariç tutarak bu değerleri yeni bir diziye atar. TreeSet, elemanları otomatik olarak sıralar
# ve tekrarlanan değerlere izin vermez. Kod, bu işlemi gerçekleştirmek için dört farklı yöntem sunar:
#
# Yöntem 1: Döngü kullanarak TreeSet'e eleman ekler.
# Yöntem 2: Arrays.asList(dizi) ile oluşturulan liste üzerinden doğrudan TreeSet oluşturur.
# Yöntem 3: addAll metodu ile liste elemanlarını TreeSet'e ekler.
# Yöntem 4: Collections.addAll metodu ile dizi elemanlarını doğrudan TreeSet'e ekler.
# Python'da benzer bir işlemi set kullanarak gerçekleştirebiliriz. Python'daki set,
# tekrar eden değerlere izin vermez ve elemanları sırasız bir şekilde saklar. Ancak,
# Python'da set elemanları otomatik olarak sıralanmaz. Sonucu sıralı bir şekilde elde etmek
# için sorted fonksiyonunu kullanabiliriz:

import random

# 10 elemanlı dizi, 0'dan 10'a kadar rastgele sayılarla doldurulur
dizi = [random.randint(0, 10) for _ in range(10)]
print("dizi =", dizi)

# Dizi elemanları bir set'e dönüştürülerek tekrarlanan değerler kaldırılır
# Sonuç sıralanarak listeye dönüştürülür
ts = sorted(set(dizi))
print("ts =", ts)


