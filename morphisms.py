def iterate(h, a='0', N=10**4):
    """
    Return the length-N prefix of the sequence obtained by iterating
    h on a.

    - h is a morphism given as a dictionary.
    - a is the letter h is iterated on.
    """
    if (not a in h.keys()) or (not h[a].startswith(a)):
        print("Cannot iterate", h, "on", a)
        return None
    aux = h[a]
    ind = 1
    while len(aux) < N:
        try:
            aux += h[aux[ind]]
        except:
            print(aux[ind], "is not in the domain of", h)
            return None
        ind += 1
    return aux[:N]

if __name__ == '__main__':
    h = {'0': '012', '1': '02', '2': '201'}
    print(iterate(h, '2', 30))
    print(iterate(h, '3', 30))
    h['2'] = '203'
    print(iterate(h, '2', 30))
