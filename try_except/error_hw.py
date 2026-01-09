try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('Error: not integer')

print()

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print('Error: Division by zero')
finally:
    print('All Done')

print()

def ask():
    while True:
        try:
            n = int(input('Input an integer: '))
            n = n**2
        except:
            print('An error occured! Please try again!')
            continue
        else:
            print(f'Thank you, your number squared is: {n}')
            break

ask()