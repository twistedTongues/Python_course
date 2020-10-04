def generator(current_time):
    sep_position = int(current_time[-1:])
    if sep_position % 5 != 0:
        sep_position %= 5
    else:
        sep_position = 5
    yield sep_position
