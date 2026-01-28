def is_prime(n, i=2):
    if n<=1:
        return False
    if i*i>n:
        return True
    if n%i==0:
        return False
    return is_prime(n,i+1)

num=12
if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")
