import random
digits = list(range(0, 100000))
password = random.randint(0, 100000)

each_digit = -1
print(password)

while each_digit!=password:
    for each_digit in digits:
        print(each_digit)
        if each_digit == password:
            print("Password is Cracked: "+str(each_digit))
            p=str(input("Enter the password: "))
