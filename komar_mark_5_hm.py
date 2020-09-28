def my_range(start, stop):
    while True:
        if start % stop == 0:
            print('Vasya')
        yield start
        start += 1


r = my_range(1, 3)
while True:
    choice = input("If u want to continue type 'y' or click enter \
to exit: ")
    if choice == 'y':
        print(next(r))
    else:
        break
