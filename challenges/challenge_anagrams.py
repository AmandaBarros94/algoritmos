def parcelling(lyrics, start, end):
    midst = lyrics[end]
    maker = start - 1

    for index in range(start, end):
        if lyrics[index] <= midst:
            maker = maker + 1
            lyrics[index], lyrics[maker] = (
                lyrics[maker],
                lyrics[index],
            )

    lyrics[maker + 1], lyrics[end] = lyrics[end], lyrics[maker + 1]

    return maker + 1

def ordain(lyrics, start, end):
    if start < end:
        p = parcelling(lyrics, start, end)
        ordain(lyrics, start, p - 1)
        ordain(lyrics, p + 1, end)

    return lyrics

def is_anagram(first, second):
    
    if (first or second) != "":
        list_1, list_2 = list(first.lower()), list(
            second.lower()
        )
        sort_1, sort_2 = ordain(list_1, 0, len(list_1) - 1), ordain(
            list_2, 0, len(list_2) - 1
        )
        string_1, string_2 = "".join(sort_1), "".join(sort_2)

        return (string_1, string_2, string_1 == string_2)

    return (first, second, False)