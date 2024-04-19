# package Gun24;
#
# import java.util.HashMap;
#
# public class _04_Map {
#     public static void main(String[] args) {
#         // Bir kartvizit uygulamasını 2 kişi için yapınız
#         // isim, email, telefonu, adres
#
#         HashMap<String, String> ZKartVizit=new HashMap<>();
#         ZKartVizit.put("isim","Zehra");
#         ZKartVizit.put("email","Zehra@gmail.com");
#         ZKartVizit.put("telefon","0505676767");
#         ZKartVizit.put("adres","Çekmeköy");
#
#         System.out.println("ZKartVizit.get(isim) = " + ZKartVizit.get("isim"));
#         System.out.println("ZKartVizit.get(email) = " + ZKartVizit.get("email"));
#
#         HashMap<String, String> EKartVizit=new HashMap<>();
#         EKartVizit.put("isim","Esma");
#         EKartVizit.put("email","esma@gmail.com");
#         EKartVizit.put("telefon","0506878787");
#         EKartVizit.put("adres","Başakşehir");
#
#         System.out.println("EKartVizit.get(isim) = " + EKartVizit.get("isim"));
#         System.out.println("EKartVizit.get(email) = " + EKartVizit.get("email"));
#
#         HashMap< String , HashMap<String, String> >  kartvizitler=new HashMap<>();
#         kartvizitler.put("Zehra", ZKartVizit);
#         kartvizitler.put("Esma", EKartVizit);
#
#         System.out.println("Zehra nın emaili = " + kartvizitler.get("Zehra").get("email"));
#         System.out.println("Zehra nın telefonu = " + kartvizitler.get("Zehra").get("telefon"));
#
#         System.out.println("Esma nın emaili = " + kartvizitler.get("Esma").get("email"));
#         System.out.println("Esma nın telefonu = " + kartvizitler.get("Esma").get("telefon"));
#     }
# }


# Python'da,
# Java'daki iç içe HashMap yapısına benzer bir şekilde iç içe sözlükler (nested dictionaries) kullanarak bu kartvizit uygulamasını
# oluşturabiliriz.

def main():
    # Zehra'nın kartviziti
    z_kartvizit = {
        "isim": "Zehra",
        "email": "Zehra@gmail.com",
        "telefon": "0505676767",
        "adres": "Çekmeköy"
    }
    print("ZKartVizit['isim'] =", z_kartvizit['isim'])
    print("ZKartVizit['email'] =", z_kartvizit['email'])

    # Esma'nın kartviziti
    e_kartvizit = {
        "isim": "Esma",
        "email": "esma@gmail.com",
        "telefon": "0506878787",
        "adres": "Başakşehir"
    }
    print("EKartVizit['isim'] =", e_kartvizit['isim'])
    print("EKartVizit['email'] =", e_kartvizit['email'])

    # Kartvizitlerin toplandığı ana sözlük
    kartvizitler = {
        "Zehra": z_kartvizit,
        "Esma": e_kartvizit
    }

    print("Zehra'nın emaili =", kartvizitler["Zehra"]["email"])
    print("Zehra'nın telefonu =", kartvizitler["Zehra"]["telefon"])
    print("Esma'nın emaili =", kartvizitler["Esma"]["email"])
    print("Esma'nın telefonu =", kartvizitler["Esma"]["telefon"])

if __name__ == "__main__":
    main()


# Java'da yaptığımız gibi kartvizit bilgilerini iç içe sözlükler kullanarak yönetmektedir.
# İlgili anahtarlar (isim, email, telefon, adres) kullanılarak değerlere erişim sağlanmaktadır ve
# kartvizitler sözlüğü, her kişinin adını anahtar olarak kullanarak kişiJava'da yaptığımız gibi
# kartvizit bilgilerini iç içe sözlükler kullanarak yönetmektedir.
# İlgili anahtarlar (isim, email, telefon, adres) kullanılarak değerlere erişim sağlanmaktadır ve kartvizitler sözlüğü,
# her kişinin adını anahtar olarak kullanarak kişisel
# kartvizit bilgilerine erişim sağlamaktadır. Bu yapı, Python'da veri yönetimi için oldukça yaygın
# ve etkili bir yöntemdir.sel kartvizit bilgilerine erişim sağlamaktadır. Bu yapı, Python'da veri
# yönetimi için oldukça yaygın ve etkili bir yöntemdir.