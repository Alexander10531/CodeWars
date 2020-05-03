import re 

def to_camel_case(text):
    match = re.findall("[-_][A-z]",text)
    for i in match:
        text = re.sub(i,i[1].upper(),text)
    return text

