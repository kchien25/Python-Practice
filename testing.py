def make_negative(number):
    if number > 0:
        print(number * -1)
    elif number < 0:
        print(number)
    elif number == 0:
        print(number)
    else:
        print("this is not a number...")

make_negative(input("please input a number: "))