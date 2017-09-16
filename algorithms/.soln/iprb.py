with open('iprb.txt') as file:
    inputs = file.readline().strip()

    k,m,n = [int(n) for n in inputs.split()]

    T = k + n + m
    p_Aa_Aa = (m/T) * ((m-1)/(T-1)) / 4
    p_Aa_aa = (m/T) * (n/(T-1))
    p_aa_aa = (n/T) * ((n-1)/(T-1))

    prob_rec = p_Aa_Aa + p_Aa_aa + p_aa_aa
    prob_dom = 1 - prob_rec

    print (prob_dom)
