fibs = {0: 0, 1: 1}

def fibonacci(N):
    if N not in fibs:
        number = fibonacci(N-1) + fibonacci(N-2)
        fibs[N] = number
    return fibs[N]

N = int(raw_input('Enter a number:'))
print fibonacci(N)
