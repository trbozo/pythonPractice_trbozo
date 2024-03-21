# // String s1="meRhaba";
# // String s2="MERhABa";
s1 = "meRhaba"
s2 = "MERhABa"

# // System.out.println("s1.equalsIgnoreCase(s2) = " + s1.equalsIgnoreCase(s2));
print(f"s1.equalsIgnoreCase(s2) = {s1.lower() == s2.lower()}")
