l = [1,1,1,1,1,1,1,1,1,1] 
k = [1,1,1,1,1,0,1,0,1,0] 
s = [] 

for (i,j) in zip(l,k): 
    if i == j: 
        s.append(10) 

print(str(sum(s)) + "%")