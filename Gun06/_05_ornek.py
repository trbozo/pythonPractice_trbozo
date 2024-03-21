# // Scanner okuStr=new Scanner(System.in);
# // Scanner okuInt=new Scanner(System.in);
# // Scanner okuBool=new Scanner(System.in);
# // System.out.print("Cadde=");
# // String cadde= okuStr.nextLine();
# // System.out.print("Sokak=");
# // String sokak= okuStr.nextLine();
# // System.out.print("PostaKod=");
# // int postaKod= okuInt.nextInt();
# // System.out.print("Ülke=");
# // String ulke= okuStr.nextLine();
# // System.out.print("Ev Sahibi misiniz(t/f) =");
# // boolean evSahibi= okuBool.nextBoolean();
# // System.out.println(cadde+" "+sokak+" "+postaKod+" "+ulke+" "+evSahibi);
cadde = input("Cadde=")
sokak = input("Sokak=")
posta_kod = int(input("PostaKod="))
ulke = input("Ülke=")
ev_sahibi = input("Ev Sahibi misiniz(t/f) =").lower() == 't'
print(f"{cadde} {sokak} {posta_kod} {ulke} {ev_sahibi}")


#f öncesiyle başlayan bir string Python'da "f-string" olarak bilinir ve
# Python 3.6 sürümünde tanıtılmıştır. f-stringler, süslü parantezler {} içinde doğrudan değişkenlerin
# ve ifadelerin kullanılmasına izin vererek string içinde dinamik ifadelerin kolayca formatlanmasını sağlar.
# f harfi stringin önüne konularak, süslü parantezler içindeki ifadelerin stringe dahil edilmeden önce
# değerlendirilip formatlanacağını belirtir.

ad = "Ahmet"
yas = 30
print(f"Benim adım {ad} ve yaşım {yas}.")


## Bu kod, "Benim adım Ahmet ve yaşım 30." çıktısını üretir.
##f-string kullanmanın avantajları:
##Kod okunabilirliğini artırır.
##str.format() metoduna göre daha hızlı çalışır.
##Süslü parantezler içinde direkt olarak değişkenlerin, aritmetik işlemlerin ve hatta metod çağrılarının kullanılabilmesi.
##Bu nedenle, f-stringler Python'da string formatlama ihtiyaçları için sıkça tercih edilir.
