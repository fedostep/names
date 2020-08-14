alp={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
def get_names():
    parts=[]
    f = open('text.txt')
    line = f.readline()
    tmp=line.split(',')
    for i in tmp:
        b=i.strip('"')
        parts.append(b)
    parts.sort()
    return parts


def get_scores(lst):
    su = 0
    c = 1
    for i in lst:
        coin = 0
        for j in i:
            coin += alp[j]
        su += coin * c
        c += 1
    return su


lst = get_names()
print(get_scores(lst))






