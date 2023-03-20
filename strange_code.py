start_time = 1
multiple = 3
look_up = 1
prev = 0
i = 1
while i < look_up:
    # print(start_time)
    temp = start_time
    start_time = start_time + (multiple*i)
    if start_time > look_up:
        print(temp)
        break

    i*=2

# print(prev)



#  A            b
# top_array = start_time - 2
# move = abs(top_array)