

def fibonacci(produced_numbers, first_number=0, second_number=1):
    if second_number < first_number:
        first_number, second_number = second_number, first_number

    if produced_numbers <= 0:
        produced_numbers = 1

    fibonacci_numbers = [first_number, second_number]
    for i in range(produced_numbers+1):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers

