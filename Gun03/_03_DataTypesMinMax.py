# // System.out.println("Byte.MIN_VALUE = " + Byte.MIN_VALUE);
# // System.out.println("Byte.MAX_VALUE = " + Byte.MAX_VALUE);
# // System.out.println("Short.MIN_VALUE = " + Short.MIN_VALUE);
# // System.out.println("Short.MAX_VALUE = " + Short.MAX_VALUE);
# // System.out.println("Integer.MAX_VALUE = " + Integer.MIN_VALUE);
# // System.out.println("Integer.MAX_VALUE = " + Integer.MAX_VALUE);
# // System.out.println("Long.MIN_VALUE = " + Long.MIN_VALUE);
# // System.out.println("Long.MAX_VALUE = " + Long.MAX_VALUE);
# // System.out.println("Double.MIN_VALUE = " + Double.MIN_VALUE);
# // System.out.println("Double.MAX_VALUE = " + Double.MAX_VALUE);
# // System.out.println("Float.MIN_VALUE = " + Float.MIN_VALUE);
# // System.out.println("Float.MAX_VALUE = " + Float.MAX_VALUE);
import sys
import numpy as np

print("Byte.MIN_VALUE =", -128)
print("Byte.MAX_VALUE =", 127)
print("Short.MIN_VALUE =", -32768)
print("Short.MAX_VALUE =", 32767)
print("Integer.MIN_VALUE =", -sys.maxsize - 1)
print("Integer.MAX_VALUE =", sys.maxsize)
print("Long.MIN_VALUE =", -
