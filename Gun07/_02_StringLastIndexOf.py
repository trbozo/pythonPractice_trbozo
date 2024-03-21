# // String cumle="Merhaba Dünya";
cumle = "Merhaba Dünya"

# // System.out.println("indexOf(a) = " + cumle.indexOf("a"));
# // System.out.println("lastIndexOf(a) = " + cumle.lastIndexOf("a"));
print(f"indexOf('a') = {cumle.find('a')}")
print(f"lastIndexOf('a') = {cumle.rfind('a')}")


##Python'da, rfind() metodu, Java'daki lastIndexOf() metoduna karşılık gelir ve aranan ifadenin en son bulunduğu indeksi döndürür.