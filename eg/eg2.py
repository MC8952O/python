print("Give me two numbers, and i'll divide them")
print("Enter 'q' to quit." )
while True:
    first_number = int(input('\nFirst number:'))
    if first_number == 'q':
        break
    second_number = int(input("Sencond number:-))
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('除数不能为0')
    else:
        print(answer)
