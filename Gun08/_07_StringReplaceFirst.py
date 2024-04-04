#Python'da replaceFirst doğrudan bir karşılığı yoktur, ancak benzer bir işlev re modülü kullanılarak sağlanabilir.
# Burada basit bir replace kullanarak ilk bulunanı değiştireceğiz.

# // String text = "Merhaba Dünya";
# // System.out.println("text.replaceFirst('a','e') = " + text.replaceFirst('a','e'));
import re
text = "Merhaba Dünya"
print(f"text.replaceFirst('a', 'e') = {re.sub('a', 'e', text, 1)}")
