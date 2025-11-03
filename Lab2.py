while True:# it will help to run program indefinitley until user quit
    num_elements=int(input("Enter the input:"))# it will ask for input in integer
    num_fizz=0
    num_buzz=0
    num_fizzbuzz=0
    for i in range(1,num_elements +1):#after input i will go through inputed value +1
        print(f"Iteration number {i}: \n",end= "" ) # printing number of iterations
        if(i%3== 0 and i%5==0):
            print("FizzBuzz")
            num_fizzbuzz +=1
        elif(i%3==0):
            print("Fizz")
            num_fizz +=1
        elif(i%5==0):
            print("Buzz")
            num_buzz +=1
        else:
            print(i)
    print(f"Total Number of Fizz: {num_fizz}")
    print(f"Total number of Buzz: {num_buzz}")
    print(f"Total number of FizzBuzz: {num_fizzbuzz}")
    ask=input("Would you like to exit? (Y/N):")
    if ask in ("Yes","Y","YES","yes","y"):
        print("Exiting, BYE")
        break
    else:
        print("Restarting")
