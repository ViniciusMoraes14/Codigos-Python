def position(string,letra):
    V = []
    for x in range(len(string)):
        if string[x] == letra:
            V.append(x)
    return V


