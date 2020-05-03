#325
from string import ascii_lowercase as aslo 
from re import sub
from collections import Counter


def is_panagram(s):
    return True if sum(list(map(aslo.index,list(Counter(sub(r"[^a-z]","",s.lower())).keys())))) == 325 else False

print(is_panagram("The quick, brown fox jumps over the lazy dog!"))
