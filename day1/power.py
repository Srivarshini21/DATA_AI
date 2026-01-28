def power(n,e):
    if e==0:
        return 1
    return n*power(n,e-1)

result = power(5,3)
print(result)
