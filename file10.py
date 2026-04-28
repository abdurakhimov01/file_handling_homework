def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    o=open(data,"r")
    f=o.read()
    p=f.split('\n')
    k=[]
    for i in p:
        k+=[len(i)]
    return max(k)
print(main("data/data10.txt"))
# Read data from file