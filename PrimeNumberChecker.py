# Prime number checker
num = 1

if num > 1:
    for i in range (2, num):
        if (num % i) == 0:
            print(num, "The number must be above 0")
            break
    else:
        print(num, "This number is prime")
else:
    print(num, "This number is not prime")
