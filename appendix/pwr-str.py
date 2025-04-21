"""Implement power-string and string concatenation."""


def cdot(a, b):
    """Concatenation of two strings."""
    return f"{a}{b}"


def K(X=None):
    """
    String concatenation - produce a table `K(X) := X * X`.

    Return a product table T with the results of string concatenation K."""
    if X is None:
        X = ["", "0", "1"]
    T = list()
    for i in range(len(X)):
        T.append(["" for k in range(len(X))])
        for j in range(len(X)):
            T[i][j] = cdot(X[i], X[j])
    return T


def uniq(X):
    """Return set as sorted list with unique items."""
    X = list(set(X))
    X.sort()
    X = list(sorted(X, key=len))
    return X


def Splt(c, S):
    """
    String split operation.
    
    Return a set of all strings that can be split from S by symbol c.

    Example:
        > Splt("","0111")
        ['', '0', '1', '01', '11', '011', '111', '0111']
    """
    if c == "":
        R = list()
        for i in range(len(S)):
            for j in range(len(S)):
                R.append(S[i:j + 1])
    else:
        raise NotImplemented(
            "Split over non-empty sub-string is not implemented.")
    return uniq(R)


def flat(T):
    """Return a union over T elements as a flat list."""
    return uniq([x for row in T for x in row])


def PwrStr(X=None):
    """
    Power string.

    Example:
    > X1 = PwrStr()
    ['', '0', '1', '00', '01', '10', '11']
    
    > X2 = PwrStr(X1)
    ['', '0', '1', 
     '00', '01', '10', '11', 
     '000', '001', '010', '011', 
     '100', '101', '110', '111', 
     '0000', '0001', '0010', '0011', 
     '0100', '0101', '0110', '0111', 
     '1000', '1001', '1010', '1011', 
     '1100', '1101', '1110', '1111']
    """
    X = flat(K(X))
    return X
