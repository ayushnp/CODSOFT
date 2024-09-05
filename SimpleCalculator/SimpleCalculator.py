import math as m

def simple_calculator(a,b,operator):
    if operator=='+':
        sum=a+b
        print(f'The sum of {a} and {b} is = ',sum)
    elif operator=='-':
        diff=a-b
        print(f'The difference of {a} and {b} is = ',diff)

    elif operator=='*':
        product=a*b
        print(f'The product of {a} and {b} is = ',product)

    elif operator=='/':
        if b==0:
            print('Denominator cannot be zero..')
        else:
            quotient=a/b
        print(f'The Quotient is = ',quotient)
    elif operator=='%':
        modulus=a%b
        print('Modulus is = ',modulus)

    elif operator=='sqrt':
        sq=m.sqrt(a)
        print(f'Square root of {a} is = ',sq)
    
    else:
        print('Invalid operator..')
    

operator=input('Enter the operator = ')
if operator=='sqrt':
    a=int(input('Enter a number = '))
    simple_calculator(a,b,operator)

else:

    a=int(input('Enter a number = '))
    b=int(input('Enter a number = '))
    
    simple_calculator(a,b,operator)

        