import random
var=random.randint(0,15)

#varが3と5の倍数のとき
if var%3==0 and var%5==0:
    print("FizzBuzz")
#varが3の倍数の時
elif var%3==0:
    print("Fizz")
#varが5の倍数の時
elif var%5==0:
    print("Buzz")
#varがいずれの条件も満たさないとき
else:
    print(var)