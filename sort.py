l=[10,5,15,6,8,9]
for i in range(len(l)-1):
    for j in range(0, len(l) - i - 1):
        if l[j]>l[j+1]:
            tem=l[j]
            l[j]=l[j+1]
            l[j+1]=tem

print("after ascending",l)



        