a = int(input("Enter the A number: "))
choice = input("Operations (+, -, *, %): ")
b = int(input("Enter the B number: "))
while True:
    if choice == '+':
        c = a + b
        C = str(c)
        print('Answer =', C)
        break
    if choice == '-':
        c = str(a - b)
        print('Answer =', c)
        break
    if choice == '*':
        c = str(a * b)
        print('Answer =', c)
        break
    if choice == '%':
        c = str(a / b)
        print('Answer = {:.2f}'.format(float(c)))
        break
