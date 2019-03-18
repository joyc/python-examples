fibs = {0: 0, 1: 1}

def fibonacci(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        number = fibonacci(N-1) + fibonacci(N-2)
        return number

N = int(raw_input('Enter a number:'))
print fibonacci(N)
