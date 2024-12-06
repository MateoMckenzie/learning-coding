
def  ctof(c):
    f = c * 9/5 + 32
    return f
c = float(input("gimme"))
print(ctof(c))


def  ftoc(f):
    c = f / 9/5 - 32
    return c
f = float(input("gimme"))
print(ftoc(f))
