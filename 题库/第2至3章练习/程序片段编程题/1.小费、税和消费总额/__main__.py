consumption = eval(input())

# blank start
tip = consumption * 0.1
# blank end
# blank start
tax = consumption * 0.07
# blank end

total = consumption+tip+tax
print("The  consumption  is  %.4f,  the  tip  is  %.4f,  the  tax  is  %.4f,so  the  total  consumption  is  %.4f" %
      (consumption, tip, tax, total))
