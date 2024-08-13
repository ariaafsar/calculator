def sum(num1 , num2) :
    resualt = num1 + num2
    print(resualt)

def sub(num1 , num2) :
    resualt = num1 - num2
    print(resualt)

def multi(num1 , num2) :
    resualt = num1 * num2 
    print(resualt)

def div(num1 , num2) :
    resualt = num1 / num2 
    print(resualt)

def main():
    while True :
        inp = input("choose your action please :\n1.sum 2.subtraction 3.multipication 4.division 5.exit\n")
        if inp == "1" or inp == "sum" :
            num1 , num2 = map(int , input("enter your numbers please : <number 1> <number 2>").split())
            sum(num1 , num2)
        elif inp == "2" or inp == "subtraction" :
            num1 , num2 = map(int , input("enter your numbers please : <number 1> <number 2>").split())
            sub(num1 , num2)
        elif inp == "3" or inp == "multipication" :
            num1 , num2 = map(int , input("enter your numbers please : <number 1> <number 2>").split())
            multi(num1 , num2)
        elif inp == "4" or inp == "division" :
            num1 , num2 = map(int , input("enter your numbers please : <number 1> <number 2>").split())
            div(num1 , num2)
        elif inp == "5" or inp == "exit" :
            break
main()