def findRoot(f,a,b,epsilon):
    m=float(0.5*(a+b))
    if abs(b-a)<epsilon:
        return(m)
    if float(f(m)) == 0:
        return(m)
    elif float(f(m))>0:
        if float(f(a))<0:
            return findRoot(f,a,m,epsilon)
        elif float(f(b))<0:
            return findRoot(f,m,b,epsilon)
    elif float(f(m))<0:
        if float(f(a))>0:
            return findRoot(f,a,m,epsilon)
        elif float(f(b))>0:
            return findRoot(f,m,b,epsilon)

list_root = []

def findAllRoots(f,a,b,epsilon):
    a, b = [min(a,b), max(a,b)]
    m = float(0.5*(a+b))
    print(m)
    input()
    if abs(float(f(m))) <= 10**(-6):
        list_root.append(m)
        return list_root
    if ((abs(b-a)<epsilon) and (a<0) and (b>0)):
        list_root.append(m)
        return list_root
    elif abs(b-a)<epsilon and b<0:  #geen oplossing
        return
    elif abs(b-a)<epsilon and a>0:  #geen oplossing
        return
    else:
        findAllRoots(f,a,m,epsilon)
        findAllRoots(f,m,b,epsilon)
    return list_root