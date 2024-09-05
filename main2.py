upper=int(input("Enter an upper range:"))
lower=int(input("Enter a lower range:"))
print("prime numbers between ",upper," and ",lower," are:")
for i in range(lower,upper+1):
    if i>1:
        for x in range(2,i):
            if (i%x)==0:
                break
        else:
            print(i)