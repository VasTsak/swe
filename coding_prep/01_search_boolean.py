def intersect(a1: list, a2 :list) -> list:
    """
    Identify the common elements of two arrays.
    
    Arguments:
        a1: list
            First list to compare
        a2: list
            Second list to compare
    Return:
        a: list
            List of common elements betwen a1 and a2
    """

    a = []
    i = 0
    j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] == a2[j]:
            a.append(a1[i])
            i += 1
            j += 1
        elif a1[i] > a2[j]:
            j += 1
        else:
            i += 1
    print(a)
    return a

def main():
    # Test 1
    t1 = intersect(a1=[1, 2, 3], a2=[2])
    assert t1 == [2], "T1: Invalid result"
    # Test 2
    t2 = intersect(a1=[-1, 2], a2=[0])
    assert t2 == [], "T2: Invalid result"
    # Test 3
    t3 = intersect(a1=[], a2=[1, 2, 3, 4, 5])
    assert t3 == [], "T3: Invalid result"
    # Test 4
    t4 = intersect(a1=[1, 2, 3, 4], a2=[1, 2, 3, 4])
    assert t4 == [1, 2, 3, 4], "T4: Invalid result"
    # Test 5
    try:
        t5 = intersect(a1=1, a2=[1, 2, 3, 4])
    except TypeError:
        print("Wrong type.")

if __name__ == "__main__":
    main()