def spin_words(sentence):
    # Your code goes here
    sol=""
    words=sentence.split(" ")
    for w in words:
        if len(w)>=5:
            w=w[::-1]
        sol+=w+" "
    return sol[:-1]