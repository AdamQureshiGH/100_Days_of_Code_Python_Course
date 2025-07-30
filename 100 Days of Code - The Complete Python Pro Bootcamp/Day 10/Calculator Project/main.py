import art
use_last_answer = ""
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
def calculator(n1, n2, operator):
    for key in operations:
        if (operator == key):
            return float(operations[key](n1, n2))
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}
print(art.logo)
n1 = 0
n2 = 0
last_answer = 0
continue_calculating = ""
while(True):
    continue_calculating = input("Would you like to continue?(y/n)").lower()
    if(continue_calculating == "n"):
        break
    if(use_last_answer == "y"):
        n1 = last_answer
    else:
        n1 = float(input("What is your first number?\n"))
    for key in operations:
        print(key)
    operator = input("What operation would you like?:\n")
    n2 = float(input("What is your second number?\n"))
    last_answer = calculator(n1, n2, operator)
    use_last_answer = input(f"The answer is {last_answer}, would you like to use this answer for the next problem (y/n)").lower()





