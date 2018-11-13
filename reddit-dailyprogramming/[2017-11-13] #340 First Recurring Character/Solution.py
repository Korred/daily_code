def first_rec(string):
    '''
    A function that outputs the first recurring character in a string (and the original position)
    If no recurring character is found return None instead
    :type x: str
    :rtype: (str, int) or None
    '''
    d = dict()

    for i, char in enumerate(string):
        if char in d:
            return (char, d[char])
        else:
            d[char] = i

    # otherwise no recurring character found
    return None

# Example use:
examples = [
    'ABCDEBC',
    'IKEUNFUVFV',
    'PXLJOUDJVZGQHLBHGXIW',
    '*l1J?)yn%R[}9~1"=k7]9;0[$'
]

for e in examples:
    print("String: {}".format(e))
    print("First Recurring Character: {} at position {}".format(*first_rec(e)))
    print()