import operator

def zero(dicti = None):
    return 0 if dicti == None else int(dicti["oper"](0,dicti["num"])) 
def one(dicti = None):
    return 1 if dicti == None else int(dicti["oper"](1,dicti["num"])) 
def two(dicti = None):
    return 2 if dicti == None else int(dicti["oper"](2,dicti["num"])) 
def three(dicti = None):
    return 3 if dicti == None else int(dicti["oper"](3,dicti["num"])) 
def four(dicti = None):
    return 4 if dicti == None else int(dicti["oper"](4,dicti["num"])) 
def five(dicti = None):
    return 5 if dicti == None else int(dicti["oper"](5,dicti["num"])) 
def six(dicti = None):
    return 6 if dicti == None else int(dicti["oper"](6,dicti["num"])) 
def seven(dicti = None):
    return 7 if dicti == None else int(dicti["oper"](7,dicti["num"]))
def eight(dicti = None):
    return 8 if dicti == None else int(dicti["oper"](8,dicti["num"]))
def nine(dicti = None):
    return 9 if dicti == None else int(dicti["oper"](9,dicti["num"]))
def plus(num):
    return {"oper":operator.add, "num": num}    
def minus(num):
    return {"oper":operator.sub, "num": num}      
def divided_by(num):
    return {"oper":operator.truediv, "num": num}      
def times(num):
    return {"oper":operator.mul, "num": num}      
