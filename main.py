string=input("please input your own word:")
char=input("pls input a single alphabet:")
i=0
count=0
while (i<len(string)):
    if string[i]==char:
        count=count+1
    i=i+1
print("the number of times",char,"has occured in your word=",count)