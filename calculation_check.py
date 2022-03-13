# addition function that makes it so that parameters a and b are added together


def add(a, b):
    answer = a + b
    text("{} + {} = {}".format(a, b, answer))


# subtraction function that makes it so that parameters a is subtracted by parameter b


def subtract(a, b):
    answer = a - b
    text("{} - {} = {}".format(a, b, answer))


# multiplication function that makes it so that parameter a is multiplied by parameter b

def multiply(a, b):
    answer = a * b
    text("{} x {} = {}".format(a, b, answer))

# division function that divides parameter a by parameter b


def divide(a, b):
    answer = a / b
    text("{} / {} = {}".format(a, b, answer))


# number function that asks users for input and will reiterate itself until the user has input a valid number


def number(message):
    while True:
        try:
            print("")
            answer = int(input(message))
            return answer
        except ValueError:
            print("")
            print("Error, enter a whole number")


# message function
# that adds spaces between messages


def text(message):
    print("""
    {}""".format(message))


# program running


text("Welcome to Calculation Check")


# will forever reiterate itself if my

while True:
    num1 = number("Enter a whole number of any value")
    num2 = number("Enter another whole number of any value")
    while True:
        response = input("Would you like to add, subtract, multiply or divide").lower()
        if response == "add":
            add(num1, num2)
        elif response == "subtract":
            subtract(num1, num2)
        elif response == "multiply":
            multiply(num1, num2)
        elif response == "divide":
            divide(num1, num2)
        else:
            print("Enter either add, subtract, multiply or divide")