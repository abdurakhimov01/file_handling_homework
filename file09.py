import string
def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data, 'r')
    p=f.read()
    l=[]
    d=string.digits
    i=0
    while i <len(p):
        j=0
        while j<len(d):
            if d[j]==p[i]:
                l.append(p[i])
            j+=1
        i+=1
    return min(l)
print(main("data/data09.txt"))
# Read data from file