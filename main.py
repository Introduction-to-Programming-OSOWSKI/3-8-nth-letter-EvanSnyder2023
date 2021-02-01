def nthLetter(w, n):

    if len(w) < n:
        return False

    else:
        return w[n]

print (nthLetter("car", 2))