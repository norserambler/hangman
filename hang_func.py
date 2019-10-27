def hang_struct(count):
    hangman=['---',' |',' O','/','|','\\','/',' \\']
    j=0
    n=3
#del hangman[3] 
#print(hangman)
#while(j<2):
    
    for i in range(0,count):
   
        if(i==3 or i==4 or i==6):
            print(hangman[i], end='')
        else:
             print(hangman[i]);     
    return        

#hang_struct()

'''def find(list1=[],x):
    for i in range(0,len(list1)):
        if(x==)
   '''     
def find(list1,inp,org):
    for i in range (0,len(org)):
        if(inp==org[i]):
            return i
