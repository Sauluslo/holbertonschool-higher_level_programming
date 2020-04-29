#!/usr/bin/python3
def fizzbuzz():
    text = ""
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            text += "FizzBuzz"
        elif n % 3 == 0:
            text += "Fizz"
        elif n % 5 == 0:
            text += "Buzz"
        else:
            text += str(n)
        if n < 101:
            text += " "
    print(text, end="")
