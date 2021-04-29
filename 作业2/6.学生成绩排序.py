import csv
sorted_score = ""

raw_data = open('./score.txt', 'r')
score = [list(item.strip().split(",")) for item in raw_data.readlines()]
score = [[int(row[1]), row[0]] + list(map(int, row[2:])) for row in score]
score.sort(key=lambda k: sum(k[2:]), reverse=True)
csv.writer(open('./sorted.txt', 'w+')).writerows(score)
