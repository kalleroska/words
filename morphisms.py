

def Iterate(h, a='0', N=10**4):
    """
    Return the length-N prefix of the sequence obtained by iterating
    h on a.

    - h is a morphism given as a dictionary.
    - a is the letter h is iterated on.
    """
    aux = h[a]
    ind = 1
    while len(aux) < N:
        aux += h[aux[ind]]
        ind += 1
    return aux[:N]

if __name__ == '__main__':
    h = {'0': '012', '1': '02', '2': '201'}
    print(Iterate(h, '2', 30))
