letter_list = [
    [" ", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/"],
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    [":", ";", "<", "=", ">", "?", "@"],
    [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ],
    ["[", "\\", "]", "^", "_", "`"],
    [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ],
    ["{", "|", "}", "~"],
]
cadr_list = [
    "cadadddddr",
    "caddadddddr",
    "caadddddr",
    "caddadddddr",
    "cadddddddddddddddddddadddddr",
    "cadddddadddddr",
    "caaddddddr",
    "cadddddddddddadddr",
    "cadadr",
    "cadddddadr",
    "cadddddddadr",
    "caddddaddddr",
    "caddddddddadr",
    "caddddadr",
    "cadddddadr",
    "cadddadr",
    "cadddadddddr",
    "caddddaddddr",
    "cadddddddddddddddadddddr",
    "cadddddddddddddddddadddr",
    "caadr",
    "caddddddadddddr",
    "cadddddddddddddddddadddr",
    "caddddadr",
    "caddddddddddddadddr",
    "caddddddddddddadddddr",
    "cadadr",
    "cadddddddddddddadddddr",
    "caddddddadddr",
    "caddddaddddr",
    "cadadr",
    "cadddddadr",
    "caddddaddddr",
    "caddddadr",
    "caddddddddddddddddddddddadddddr",
    "cadddadr",
    "caddddddddddddddddddadddr",
    "caadr",
    "caddddddddddddadddr",
    "caddddadddddr",
    "cadar",
    "caddaddddddr",
]

flag = ""
for i in cadr_list:
    curlist = letter_list
    for reg in reversed(i):
        if reg == "d":
            curlist = curlist[1:]
        elif reg == "a":
            curlist = curlist[0]

    flag = flag + curlist
print(flag)
