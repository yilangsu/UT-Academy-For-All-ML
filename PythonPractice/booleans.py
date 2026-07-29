def paycheck(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        if hours > 55:
            print("too many hours worked!")
        return 100 + hours * rate
    

print(paycheck(65, 2.34))

