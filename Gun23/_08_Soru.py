# package Gun23;
#
# import java.util.HashSet;
#
# public class _08_Soru {
#     public static void main(String[] args) {
#         // 1 de 20 ye kadar (20 dahil) olan sayılardan random olarak
#         // tekrar olmayacak şekilde 10 tane sini bir diziye atayınız
#         // yani 10 tane random sayı istiyoruz ama içinde tekrar
#         // olmayacak
#
#         HashSet<Integer> sayilar= new HashSet<>();
#
#         while( sayilar.size() < 10){ //10 olduğunda duracak
#
#             int rndSayi=(int)(Math.random()*20)+1;
#
#             sayilar.add(rndSayi);
#
#         }
#
#         System.out.println("sayilar = " + sayilar);
#     }
# }


# Bu Java kodu, 1 ile 20 (20 dahil) arasındaki sayılardan rastgele seçilmiş,
# tekrarsız 10 adet sayıyı bir HashSet içinde saklar. HashSet, tekrar eden değerleri kabul etmediği için bu kod parçası,
# her bir sayıyı yalnızca bir kez ekler. Kod, sayilar adındaki HashSetin boyutu 10 olana kadar rastgele sayılar üretir
# ve bunları sete ekler. Bu işlem, setin boyutu 10'a ulaşana kadar devam eder.
#
# Math.random() fonksiyonu, 0.0 ile 1.0 arasında rastgele bir değer üretir (1.0 hariç).
# Bu değer, *20 ile çarpılarak 0 ile 19 arasında bir değer elde edilir ve +1 ile bu değer
# 1 ile 20 arasına dönüştürülür. Sonuç, bir tam sayıya dönüştürülür (int cast) ve sayilar setine eklenir.
#
# Python'da bu işlemi gerçekleştirmek için benzer bir yaklaşım izlenebilir.
# Python'da random.sample() fonksiyonu, belirli bir aralıktan rastgele,
# tekrarsız değerler seçmek için daha uygun olabilir:
#
# Python'da Benzer İşlem;


import random

# 1'den 20'ye kadar olan sayılardan rastgele, tekrarsız 10 adet sayı seç
sayilar = random.sample(range(1, 21), 10)

print("sayilar =", sayilar)


#Bu Python kodu, 1 ile 20 (dahil) arasında rastgele,
# tekrarsız 10 adet sayı üretir ve ekrana yazdırır. random.sample() fonksiyonu,
# birinci parametre olarak verilen aralıktan (range(1, 21)), ikinci parametre olarak belirtilen adet kadar (10) rastgele,
# tekrarsız sayı seçer.
# Bu yöntem, belirtilen aralıktan istenen sayıda tekrarsız rastgele sayı seçmek için oldukça pratiktir.