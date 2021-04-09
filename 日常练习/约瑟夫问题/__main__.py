m = int(input("m:"))
n = int(input("n:"))
m_queue = list(range(1, m + 1))
index = 0
while True:
    if len(m_queue) < n:
        break
    index += n - 1
    if index > len(m_queue) - 1:
        index = index % (len(m_queue))
    print(m_queue[index])
    del m_queue[index]
