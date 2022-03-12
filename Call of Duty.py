a=input('Enter Username :')
x=float(input("Enter your score:"))
a=x*2.5
if x>=500 and x<=1000 :
        d=(a/10)
        print("You won $:",d)

elif x>=1001 and x<=1500 :
        e=(a/5)
        print("You won $:",e)

elif x>=1501 and x<=2500 :
        f=(a/4)
        print("You won $ :",f)

elif x>=2501 and x<=4500 :
        g=(a/2)
        print("You won $ :",g)

else :
       print("INVALID INPUT")       
