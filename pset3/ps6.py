def max_val(t):
    list_of_ints = []

    def parseInts(val):
        for item in val:
            if type(item) is int:
                list_of_ints.append(item)
            else:
                parseInts(item)

    parseInts(t)

    return max(list_of_ints)



max_val([[30],[2, 8]])