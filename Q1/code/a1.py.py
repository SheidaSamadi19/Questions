# Authors: Sheida Samadi , Baran Farrokhian

# Input numbers
a = float(input('enter the first number : '))
b = float(input('enter the second number : '))
c = float(input('enter the third number : '))
d = float(input('enter the fourth number : '))
e = float(input('enter the fifth number : '))

# Sum
Sum = a + b + c + d + e

# Average
av = Sum/5
list =[a,b,c,d,e]

#Library
import statistics
vari=statistics.variance(list)

# Conditions
if  0<=a<=1  and  0<=b<=1  and  0<=c<=1  and  0<=d<=1  and  0<=e<=1:
    print ( 'average is : ' , av )
    print ('variance is : ' )
    print(vari)
else:
    print ("please enter the numbers between 0 and 1 (0 and 1 it's count as well) ")
    
    
    
    
    