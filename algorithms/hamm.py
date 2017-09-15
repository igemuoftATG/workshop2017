with open("hamm.txt") as file:
    count = 0
    s1 = file.readline()
    s2 = file.readline()
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count+=1
    print count
