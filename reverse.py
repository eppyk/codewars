def reverse_words(str):
    words = str.split(" ")

    for i in range (0, len(words)):
        print words[i]
        wordie = words[i]
        words[i] = wordie[::-1]
        output = ' '.join(words)


    return output


reverse_words("bz op ul")
