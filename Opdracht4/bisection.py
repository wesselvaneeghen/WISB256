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
