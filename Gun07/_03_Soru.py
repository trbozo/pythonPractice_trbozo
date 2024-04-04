# // Scanner oku=new Scanner(System.in);
# // System.out.print("Adınız ve Soyadınız=");
# // String adSoyad=oku.nextLine();
# // char ilkHarf = adSoyad.charAt(0);
# // int boslukIndex=adSoyad.indexOf(" ");
# // char soyadIlkHarf= adSoyad.charAt(boslukIndex+1);
# // System.out.println(ilkHarf+"."+soyadIlkHarf+".");
ad_soyad = input("Adınız ve Soyadınız=")
ilk_harf = ad_soyad[0]
bosluk_index = ad_soyad.find(" ")
soyad_ilk_harf = ad_soyad[bosluk_index + 1]
print(f"{ilk_harf}.{soyad_ilk_harf}.")


# Java kodunun Python'a dönüştürülmüş hali

# Girilen bir ad soyadı örneğin "Ismet Temur" -> I.T. şeklinde yazdırınız.

ad_soyad = input("Adınız ve Soyadınız=")

ilk_harf = ad_soyad[0]  # ilk harfi al
bosluk_index = ad_soyad.index(" ")  # ilk boşluk karakterinin index'ini bul
soyad_ilk_harf = ad_soyad[bosluk_index + 1]  # soyadın ilk harfini al

print(ilk_harf + "." + soyad_ilk_harf + ".")
