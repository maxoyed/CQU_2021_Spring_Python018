exchange_rate = 6.78
currency = input()
first_char = currency[0]

if first_char in ["&", "$"]:
    if first_char == "&":
        result = float(currency[1:]) / exchange_rate
        print(f"${result:.2f}")
    else:
        result = float(currency[1:]) * exchange_rate
        print(f"&{result:.2f}")
elif first_char in ["R", "U"]:
    if first_char == "R":
        result = float(currency[3:]) / exchange_rate
        print(f"USD{result:.2f}")
    else:
        result = float(currency[3:]) * exchange_rate
        print(f"RMB{result:.2f}")
else:
    print("Error")
