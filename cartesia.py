def isValidWalk(walk):
    norths = walk.count("n")
    souths = walk.count("n")
    easts = walk.count("n")
    wests = walk.count("n")

    print len(walk)

    if len(walk) == 10:
        if norths == souths and easts == wests:
            return True
        else:
            return False
    else:
        return False


print isValidWalk(["n", "s"])
