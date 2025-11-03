"""print("Hello world!!") # how to string print we can use single quote
print(1+2) # arthimatic operations
print(4-5) # operation minus
print(4*4) # multiplication
print(5/2) # division 
print(4//2) # rounded integer
# it prints zero divison error print(4/0) 
print(2**3) # exponential 
print(10/2.0)# floats 
print('I am very beautiful\'s') # adding space 
print("I said: \n\t i would love it") # new line and tab
print("Harneet" + "Sukhchain") # Concatination two strings
print("Harneet is"+str(10) + " old") # concatination of string and integer
print("1" + "0" *3) #exponential
print("Hatneey\n" *2) #prints 2 time the name
print(str(12)+ str(2))
x=5 # variable as number
print(x+6)
print("x value is: ", x)
print(type(x))
x="Harnetet" # assigning variable 
print("Variable is number:",x)
print(type(x)) # finds type of variable
del x # can use to delete 
#print(x)
y=8
y+=6# similar way to write y=y+6
print(y)
order="Butter"
order+="\nadd bread as well"
print(order)
c=8
c-=2
print(c)
x,y,z= "Orange","Blue","Green"
print(x,y,z)
name="Kiran"
age= 34
print(f"my name is {name} and i am {age} yeras old")# formatting string
#print(f"my name is {name.upper()} and i am {age.replace('2','2')} years old")
print(f"formatted floats {(0.2+0.2):0.2f}") # formated float
myboolen=True
print(myboolen)
print(2==3) # if == is equal
print(1 !=2) # if not equal !=
print(2>1) # greater or not greater
print(3<1)
print(3>=3.1)
print(bool("hello"))
print(bool(12))"""
"""if(1>2): # if statement
    print("greater")
print("gucks")
x=1
if(x>2):
    print("True")
    if(x<2):
        print("False")
while True:
    x=int(input("Enetr any numner:"))
    y=int(input("Enter second number:"))
    if(x>y):
        print(f"first number {x} is greater than {y}")
    elif(x==y):
        print(f"Both {x} and {y} are eqyal")
        continue
    else:
        print(f"second number{y} is greater tha {x}")
        continue_loop=input("do you want to continue: ")
        if(continue_loop.lower()=="n"):
            print("Fuck you")
            break"""
fruit=["har","jaja","gsgs"]
length=len(fruit)
index=0
while(index< length):
    print(fruit[index])
    index=index+1
print("Exit")

"""print(fruit[1][0])# it works as the index number
num=[1,2,3,4,5]
print(num)
num[2]=10
print(num[2])

num.append(30)
print(num.index(2))"""
