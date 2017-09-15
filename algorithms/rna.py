with open("rna.txt") as file:
    s1 = file.read()[:-1]
    s2 = ''
    for c in s1:
        if c == 'T':
            s2 = s2 + 'U'
        else:
            s2 = s2 + c
    print s2
