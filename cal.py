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

def remain(num1 , num2) :
    resualt = num1 % num2
    print(resualt)

def sqrt(num1) :
    resualt = num1 ** 0.5
    print(resualt)

def inpoewer(num1 , num2) :
    resualt = num1 * num2
    print(resualt)

def percent(num1 , num2) :
    resualt = (num2 / 100)*num1
    print(resualt)

def main():
    while True :
        inp = input("choose your action please :\n1.sum\n2.subtraction\n3.multipication\n4.division\n5.remain\n6.square root\n7.in power\n8.percent\n9.exit\n ")
        if inp == "1" or inp == "sum" :
            num1 , num2 = map(int , input("enter your numbers please : <number 1> <number 2> \n").split())
            sum(num1 , num2)
        elif inp == "2" or inp == "subtraction" :
            num1 , num2 = map(int , input("enter your numbers please : <number 1> <number 2> \n").split())
            sub(num1 , num2)
        elif inp == "3" or inp == "multipication" :
            num1 , num2 = map(int , input("enter your numbers please : <number 1> <number 2> \n").split())
            multi(num1 , num2)
        elif inp == "4" or inp == "division" :
            num1 , num2 = map(int , input("enter your numbers please : <number 1> <number 2> \n").split())
            div(num1 , num2)
        elif inp == "5" or inp == "remain" : 
            num1 , num2 = map(int , input("enter your numbers please : <number 1> <number 2> \n").split())
            remain(num1 , num2)
        elif inp == "6" or inp == "square root" :
            num1 = map(int , input("enter your numbers please : \n"))
            sqrt(num1)
        elif inp == "7" or inp == "in power" :
            num1 , num2 = map(int , input("enter your numbers please : <number 1> <number 2> \n").split())
            inpoewer(num1 , num2)
        elif inp == "8" or inp == "percent" :
            num1 , num2 = map(int , input("enter your numbers please : <number 1> <number 2> \n").split())
            percent(num1 , num2)
        elif inp == "9" or inp == "exit" :
            break
main()