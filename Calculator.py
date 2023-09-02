def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b

a=int(input('Please enter your first number: '))
b=int(input('Please enter your second number: '))

option=int(input('''
1.Add
2.Subtract
3.Divide
4.Multiply
5.Exit
'''))

while option!=5:
    if option==1:
        print(plus(a,b))
        
        a=float(input('Please enter your first number: '))
        b=float(input('Please enter your second number: '))
        option=int(input('''
        1.Add
        2.Subtract
        3.Divide
        4.Multiply
        5.Exit
        '''))
    elif option==2:
        print(minus(a,b))
        
        a=float(input('Please enter your first number: '))
        b=float(input('Please enter your second number: '))
        option=int(input('''
        1.Add
        2.Subtract
        3.Divide
        4.Multiply
        5.Exit
        '''))
    elif option==3:
        print(divide(a,b))
        
        a=float(input('Please enter your first number: '))
        b=float(input('Please enter your second number: '))
        option=int(input('''
        1.Add
        2.Subtract
        3.Divide
        4.Multiply
        5.Exit
        '''))
    elif option==4:
        print(multiply(a,b))
       
        

    

    