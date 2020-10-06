operator = input()
a = int(input())
b = int(input())


def operation_with_a_b(operator, a, b):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = a // b
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    return result


print(operation_with_a_b(operator , a , b))