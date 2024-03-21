# // Scanner oku=new Scanner(System.in);
# // System.out.print("Öğrenci misiniz ? =");
# // boolean cevap=oku.nextBoolean();
# // System.out.println("cevap = " + cevap);
cevap = input("Öğrenci misiniz ? (e/h)=").lower() == 'e'
print("cevap =", cevap)

#.lower() Python'da bir string (metin) metodudur ve metnin tüm harflerini küçük harfe çevirir.
# Bu yöntem, genellikle kullanıcı girişlerini karşılaştırırken veya işlerken büyük/küçük
# harf duyarlılığını ortadan kaldırmak için kullanılır. == operatörü ise iki değerin eşit olup olmadığını
# kontrol eder. Yani .lower() == 'e' ifadesi, kullanıcının girdiği metni küçük harfe çevirir ve
# bu metnin 'e' harfi ile eşit olup olmadığını kontrol eder. Bu sayede, kullanıcı 'E' veya 'e' girse bile,
# her iki durumda da koşul doğru olarak değerlendirilir.

##Örneğin, kullanıcıdan bir soruya "Evet" veya "Hayır" yanıtı alıyorsanız ve
# büyük/küçük harf duyarlılığını göz ardı etmek istiyorsanız, şu şekilde bir kod yazabilirsiniz:

cevap = input("Öğrenci misiniz? (E/H): ").lower()
if cevap == 'e':
    print("Kullanıcı 'Evet' dedi.")
elif cevap == 'h':
    print("Kullanıcı 'Hayır' dedi.")
else:
    print("Geçersiz giriş.")


# Bu kod parçası, kullanıcının "E", "e", "H", veya "h" harflerinden herhangi birini girmesine izin verir
# ve girdiyi küçük harfe çevirerek karşılaştırma yapar. Böylece, programın büyük/küçük harf
# duyarlılığından etkilenmeden istenilen kontrolü yapması sağlanır.