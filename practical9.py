# ==========================================
# Program 1: Stack Implementation
# ==========================================

stack = []

# Push operation
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Pop operation
stack.pop()

print("After pop:", stack)

# Peek operation
print("Top element:", stack[-1])


# ==========================================
# Program 2: Infix to Postfix
# ==========================================

def precedence(op):
    if op == '+' or op == '-':
        return 1

    if op == '*' or op == '/':
        return 2

    return 0


def infix_to_postfix(expression):
    stack = []
    result = ""

    for char in expression:

        # If character is an operand
        if char.isalnum():
            result += char

        # If opening bracket
        elif char == '(':
            stack.append(char)

        # If closing bracket
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()

            if stack:
                stack.pop()

        # If operator
        else:
            while stack and stack[-1] != '(' and \
                    precedence(stack[-1]) >= precedence(char):
                result += stack.pop()

            stack.append(char)

    # Pop remaining operators
    while stack:
        result += stack.pop()

    return result


# Test the program
expr = "A+B*C"

print("\nInfix Expression:", expr)
print("Postfix:", infix_to_postfix(expr))