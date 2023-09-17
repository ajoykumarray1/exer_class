# t=int(input("enter how many toule you want to add:"))
# tlist=[]
# for i in range(t):
#     i=int(input("enter value in tuple:"))
#     tlist.append(i)
# print("the list is :",tlist)
# tple=tuple(tlist)
# print("the tuple is :",tple)
z=15
i=0   
while i<z:
    if(i==3):
       continue
    if (i==4):
       i+=2
    if (i==5):
      i+=4
    print(i)
    if (i==11):
       break
    i=i+1
print(i)