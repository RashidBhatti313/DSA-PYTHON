def is_balanced(expression):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            
            top_element = stack.pop()


            if opening_brackets.index(top_element) != closing_brackets.index(char):
                return False
            
    return not stack

expression1 = "{[()]}"

if is_balanced(expression1):
    print(f"The expression '{expression1} has balanced parentheses.." )
else:
    print(f"The expression '{expression1} does not have balanced parentheses..")
        
