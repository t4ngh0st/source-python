i = 0
while(i < 20):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print(i, " adalah bilangan prima")
    i = i + 1