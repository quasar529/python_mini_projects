# 숫자 맞추기 게임.
# 1부터 100까지 임의, 높은지 낮은지 알려줌

import random

num = random.randint(1, 100)
cnt = 1
while True:
    try:
        user = int(input("guess random number: "))
        if(user > num):
            print("your number is too high, try again.")
            cnt += 1
        elif(user < num):
            print("your number is too low, try again.")
            cnt += 1
        elif(user == num):
            print("You are Right. your attempts are", cnt)
            break
    except:
        print("Wrong Input, Enter a number")
