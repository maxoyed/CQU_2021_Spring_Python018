male_num = int(input())
female_num = int(input())
total_num = male_num + female_num
male_ratio = male_num / total_num * 100
female_ratio = female_num / total_num * 100
print("The male students ratio is {:.2f}%,the female students ratio is {:.2f}%".format(
    male_ratio, female_ratio))
