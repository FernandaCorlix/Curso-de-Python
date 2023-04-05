def Expand(v):
    copia = v.copy()
    arregloBi = []
    for x in range(len(v)):
        var = v[x]+1
        if(var > len(v)):
           continue
        v[x] = var
        arregloBi.append(v)
        v = copia.copy()
    return arregloBi

V = [1,1,1,1]
arr = Expand(V)
print(V)