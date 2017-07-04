# This is the collatz sequence rnsing

def collatz(number):
    global r
    if number % 2 == 0: #if number is even
        number = number // 2
        r = number
        print(number)
    elif number % 2 == 1: #if number is odd
        number = 3 * number + 1
        r = number
        print(number)

def main():
    global r
    while True:
        print('This is the program for the collatz sequence')
        try: # for error handling 
            r = eval(input("Please enter a number > 1: "))
        except NameError:
            print('ERROR:This is not an integer')
            continue
        print(r)
        if r <=1:
            continue
        elif r > 1:
            break
    while r != 1:
        collatz(r)
       
        
main()       

