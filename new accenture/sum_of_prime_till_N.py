def sum_prime(n):
    sum = 0
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for i in range(1,n):
        if is_prime(i):
            sum += i
    return sum            
answer = sum_prime(100)
print(answer)