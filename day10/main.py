import pyfiglet
import operator

print(pyfiglet.figlet_format("Calculator"))

equation = input("Please enter what you want to calculate: ")

op1, op2, op = "", "", ""
decimal_found = False

for i in equation:
    if i.isdigit() or (i == "." and not decimal_found):
        if op == "":
            op1 += i
        else:
            op2 += i
        if i == ".":
            decimal_found = True
    else:
        op += i
        decimal_found = False

# Convert operands to int or float based on presence of decimal point
if "." in op1:
    op1 = float(op1)
else:
    op1 = int(op1)

if "." in op2:
    op2 = float(op2)
else:
    op2 = int(op2)

# Define supported operators
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

# Check if the operator is supported and perform the calculation
if op in operators:
    result = operators[op](op1, op2)
    print(f"The answer is: {result}")
else:
    print("Unsupported operator")
