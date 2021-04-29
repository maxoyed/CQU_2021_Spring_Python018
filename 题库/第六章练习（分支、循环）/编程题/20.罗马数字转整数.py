string = input()
revert_rule = [['IV', 4], ['IX', 9], ['XL', 40], ['XC', 90], ['CD', 400], ['CM', 900], [
    'I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100], ['D', 500], ['M', 1000]]

for rule in revert_rule:
    string = string.replace(rule[0], f'{rule[1]} ')

result = [int(i) for i in string.strip().split(' ')]
print(sum(result))
