def evaluate_postfix(expression):
    stack = []

    def perform_operation(opertor, operand1, operand2):
        if opertor == "+":
            return operand1 + operand2
        elif opertor == "-":
            return operand1 - operand2
        elif opertor == "*":
            return operand1 * operand2
        elif opertor == "/":
            return operand1 / operand2
        
    for symbols in expression:
        if symbols.isdigit():
            stack.append(int(symbols))
        elif symbols in {"+", "-", "*", "/"}:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(symbols, operand1, operand2)
            stack.append(result)

    return stack.pop()

postfix_expression = "34+5*"
result = evaluate_postfix(postfix_expression)
print(f"The result of the postfix expression '{postfix_expression}' is: {result}")

