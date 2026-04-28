import string
def main(filename):
    o=open(filename,"r")
    f=o.read()
    l=string.ascii_letters
    d=string.digits
    i=0
    k=0
    g=0
    while i < len(f):
        j=0
        while j<len(l):
            if l[j]==f[i]:
                g+=1
            elif j <len (d) and d[j]==f[i]:
                k+=1
            j+=1
        i+=1
    return [k,g]
print(main("data/data05.txt"))