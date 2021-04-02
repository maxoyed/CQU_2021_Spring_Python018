# input language and math score
language = int(input())
math = int(input())
if language >= 99 and math >= 99:
    print("You won a scholarship of 500 yuan!")
if language < 30 and math  < 30:
    print("You need to relearn!")
