import hang_func as h
a="committee"
list1=['_','_','_','_','_','_','_','_','_']
print(list1)
i=0
j=0
n=0
flag=0
count=0

while(n==0):
     x=input("\nEnter char")
    


     for k in range(0,len(a)):
        if (x==a[k]):
            list1[k]=x
            flag=1
        elif(x[0]==' 'and x[1]==a[k]):
            list1[k]=x[1]
            flag=1 
        continue
     print(list1)
     if (flag==1):
         i=i+1
         for l in range (0,len(list1)):
             
             if (list1[l]=="_"):
                 count=count+1
                 
         #print(count)
         if(count==0):
             print("You Won")
             break
         
         else:
             
             h.hang_struct(j)
             flag=0
         count=0
     else:
         j=j+1
         h.hang_struct(j)

     if(j==8):
         print("Lost")
         print("The word is:",a)
         break
        
