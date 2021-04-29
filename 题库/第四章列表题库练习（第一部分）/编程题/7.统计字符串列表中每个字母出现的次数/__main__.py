input_str = "".join(eval(input()))

character_list = list(set(input_str))
character_list.sort()
for character in character_list:
    print(character, end=",")
    print(input_str.count(character))
