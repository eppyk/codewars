def cooking_time(eggs):
    if eggs == 0:
        return 0
    if eggs < 8:
        return 5
    else:
        rounds = eggs/8
        if eggs%8 != 0:
            rounds = rounds + 1
        return rounds*5


cooking_time(38)
