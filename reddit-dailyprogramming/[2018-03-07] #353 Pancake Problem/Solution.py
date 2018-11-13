examples = [
    "3 1 2",
    "7 6 4 2 6 7 8 7",
    "11 5 12 3 10 3 2 5",
    "3 12 8 12 4 7 10 3 8 10"
]

def flip(stack, i):
    return stack[:i] + stack[i:][::-1]

def sort_pancakes(stack):
    stack = list(stack)
    expected = sorted(stack)
    flips = 0
    pos = 0

    while stack != expected:
        
        substack = stack[pos:]
        smallest = min(substack)
        smallest_idx = substack.index(smallest)

        if smallest_idx == 0:
            pos += 1
        
        elif smallest == substack[-1]:
            stack = flip(stack, pos)
            flips += 1
            pos += 1

        else:
            stack = flip(stack, smallest_idx+pos)
            flips += 1
    
    return flips





for e in examples:
    stack = list(map(int, e.split()))
    flips = sort_pancakes(stack)
    print(f"{flips} flips used for {stack} to create {sorted(stack)}!")
    

