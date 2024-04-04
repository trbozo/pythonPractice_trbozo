# Java kodunun Python'a dönüştürülmüş hali

# EndsWith("")  : verilen karakter/ler ile bitiyor mu ?
# boolean

text = "Manisa"

print("text.endswith('sa') =", text.endswith('sa'))  # True
print("text.endswith('a') =", text.endswith('a'))    # True
print("text.endswith('Ma') =", text.endswith('Ma'))  # False


#Java'daki endsWith() metodunun karşılığı olan endswith() metodu Python'da da bulunmaktadır.
# Ancak, Java'da olduğu gibi bir dizeyi kontrol ederken endsWith() metodunu kullanmak yerine,
# Python'da daha genel olarak dize dilimleme ve karşılaştırma işlemleri kullanılabilir.
# Bu yöntemler, Python'da daha yaygın ve doğrudan uygulanabilir olduğundan tercih edilebilir.