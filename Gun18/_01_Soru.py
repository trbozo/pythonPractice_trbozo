# // package Gun18;
#
# // import java.util.Arrays;
# // import java.util.Scanner;
#
# // public class _01_Soru {
# //     public static void main(String[] args) {
# //         // 10 elemanlı bir diziyi random(10 dahil sayılarla) doldurduktan sonra,
# //         // kullanıcının gireceği bir rakamı arattırınız.
# //         // bu rakam var ise indexini yazdırınız.
#
# //         int[] dizi=new int[10];  // 10 elemanlı bir dizi tanımladım
#
# //         for (int i = 0; i < dizi.length; i++)
# //             dizi[i] = (int)(Math.random()*11);  // dizinin elemanlarını random doldurdum
#
# //         Scanner oku=new Scanner(System.in);
# //         System.out.print("Aranacak sayı(0-10)= ");
# //         int arananRakam=oku.nextInt(); // kullanıcıdan gireceği bir rakamı aldık
#
# //         for (int i = 0; i < dizi.length; i++) { // aranan rakam dizi de var mı
# //             if (dizi[i] == arananRakam)
# //                 System.out.println("Sayı var, oda numarası(indexi)"+i);
# //         }
#
# //         System.out.println("dizi = " + Arrays.toString(dizi));
# //     }
# // }


import random

# 10 elemanlı bir dizi oluştur ve 0-10 arası rastgele sayılarla doldur
dizi = [random.randint(0, 10) for _ in range(10)]

# Kullanıcıdan aranacak sayıyı al
aranan_rakam = int(input("Aranacak sayı (0-10)= "))

# Dizide aranan sayının olup olmadığını kontrol et ve varsa indexini yazdır
bulundu_mu = False
for i, sayi in enumerate(dizi):
    if sayi == aranan_rakam:
        print(f"Sayı var, oda numarası (indexi) = {i}")
        bulundu_mu = True
        break  # Sayı bulunduğunda döngüyü sonlandır

if not bulundu_mu:
    print("Sayı dizide yok.")

# Diziyi yazdır
print("dizi =", dizi)


#Java'daki işlevselliğe benzer şekilde çalışır. random.randint(0, 10) fonksiyonu,
# 0 ile 10 arası rastgele bir tam sayı üretir. enumerate(dizi) fonksiyonu,
# dizinin hem elemanlarını hem de indekslerini döner, böylece her eleman için hem değeri hem de konumu kontrol edilir.
# Aranan sayı bulunduğunda döngü break ile sonlandırılır, eğer sayı dizide yoksa kullanıcıya uygun bir mesaj gösterilir.