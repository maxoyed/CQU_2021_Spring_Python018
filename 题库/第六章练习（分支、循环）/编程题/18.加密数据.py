raw_number = [int(i) for i in list(input())]
password = [(i + 5) % 10 for i in raw_number]
password.reverse()
password = [str(i) for i in password]
print(''.join(password))
