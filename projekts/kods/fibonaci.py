fib = [0,1]
for i in range(2,100):
    fib.append(fib[-1] + fib[-2])

print(list(reversed(fib)))