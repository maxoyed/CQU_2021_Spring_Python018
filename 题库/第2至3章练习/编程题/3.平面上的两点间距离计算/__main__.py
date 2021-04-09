import math
A = list(map(float, input().split(",")))
B = list(map(float, input().split(",")))
distance = math.sqrt(
    math.pow(
        abs(A[0] - B[0]),
        2
    )
    +
    math.pow(
        abs(A[1] - B[1]),
        2
    )
)
print("{:.2f}".format(distance))
