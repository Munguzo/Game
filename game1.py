secret = 8
num1 = 0
limit = 3
while num1 < limit:
    estimate = int(input("Estimate: "))
    num1 += 1
    if estimate == secret:
        print("Awesome, you WIN!!!")
        break
else:
    print("Sorry, You fail")