import string
def main(filename):
    o=open(filename,"r")
    f=o.read()
    d=string.digits
    l=string.ascii_letters
    i=0
    k=0
    g=0
    for i in f:
        if i in string.digits:
            k+=1
        elif i in string.ascii_letters:
            g+=1
    return k,g
print(main("data/data05.txt"))