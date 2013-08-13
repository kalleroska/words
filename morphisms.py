def iterate(h, a='0', N=10**4):
    """
    Return the length-N prefix of the sequence obtained by iterating
    h on a.

    - h is a morphism given as a dictionary.
    - a is the letter h is iterated on.

    Example:
    >>> h = {'0': '012', '1': '02', '2': '201'}
    >>> print(iterate(h, '2', 30))
    201012020120220101220101202201
    """
    if (not a in h.keys()) or (not h[a].startswith(a)):
        print("Cannot iterate", h, "on", a)
        return None
    aux = h[a]
    ind = 1
    try:
        while len(aux) < N:
                aux += h[aux[ind]]
                ind += 1
    except:
        print(aux[ind], "is not in the domain of", h)
        return None
    return aux[:N]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
