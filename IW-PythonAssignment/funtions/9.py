def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("%s is not prime number" % num)
                break
        else:
            print("%s is  prime number" % num)


n = int(input("Enter a number: "))
check_prime(n)