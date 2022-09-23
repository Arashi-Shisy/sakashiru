def hikaku(l,k):
    rate = 0

    for (i,j) in zip(l,k):
        if i == j:
            rate += 10
    return(str(rate) + "%")