import re
from fractions import Fraction

number = input("input a number: ")
match = re.match(r"(\d+)?([\u00bc-\u00be])?", number)
if not match:
    print(float(number))

whole = match.group(1)
frac = match.group(2)

print(frac)

value = 0
if whole:
    value += int(whole)
if frac:
    value += float(Fraction(frac))

print(value)