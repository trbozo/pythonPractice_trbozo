# Java'daki kodun Python'a dönüştürülmüş hali

# Python'da dizeyi başlangıç önekiyle kontrol etmek için
# basitçe dizeyi dilimleme veya başlangıçtaki karakterleri kontrol etmek
# gibi yöntemler kullanılır. StartsWith() metodunun doğrudan eşdeğeri yoktur.

text = "Manisa"

# 'M' ile başlıyor mu?
print("text.startswith('M') =", text.startswith('M'))  # True

# 'Man' ile başlıyor mu?
print("text.startswith('Man') =", text.startswith('Man'))  # True

# 'ni' ile başlıyor mu?
print("text.startswith('ni') =", text.startswith('ni'))  # False


# Metodun Yokluğu: Java'da startsWith() gibi özel bir metot kullanılırken, Python'da böyle bir özel metodun doğrudan eşdeğeri yoktur. Bunun yerine, dize yöntemleri ve dil özellikleri kullanılarak benzer bir işlevsellik elde edilir.
#
# Dil Yapısı Farklılıkları: Python ve Java, farklı dil yapılarına sahiptir. Bu nedenle, kodun dönüştürülmesi sırasında bazı sözdizimi farklılıkları ve dil özellikleri göz önünde bulundurulmalıdır.
#
# Yukarıdaki Python kodu, Java kodunun temel işlevselliğini Python'a uyarlamaktadır. Python'un daha basit ve esnek dize işleme yöntemlerinden faydalanılarak aynı sonuç elde edilir.