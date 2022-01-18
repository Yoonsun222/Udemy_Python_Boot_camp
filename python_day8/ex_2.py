n = int(input("Check this number: "))

def prime_checker(number=n):
    
    cnt = 0
    if number == 1:
        return print("It's not a prime number.")

    for j in range(1,int(n**(1/2))+1):
        if n % j == 0:
            cnt += 1
    if cnt == 1:
        return print("It's a prime number.")
    else:
        return print("It's not a prime number.")

prime_checker()