# // String text="Merhaba12 Dünya23";
# // System.out.println("0-9 ->   = " + text.replaceAll("[0-9]",""));
text = "Merhaba12 Dünya23"
import re
print(f"text.replaceAll('[0-9]', '') = {re.sub('[0-9]', '', text)}")



#Python'da re modülü, regex (düzenli ifadeler) kullanımını sağlar ve replaceFirst gibi işlemler için kullanılabilir.