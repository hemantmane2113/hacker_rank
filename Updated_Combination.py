def combinations(word, size):
    word = sorted(word)   # keep in alphabetical order
    result = []

    # helper function (recursion)
    def backtrack(start, current):
        if 1 <= len(current) <= size:   # only add if not empty
            result.append("".join(current))

        for i in range(start, len(word)):
            backtrack(i + 1, current + [word[i]])

    backtrack(0, [])
    return result


# Main program
word = input().strip().upper()   # HACK
size = int(input())              # 2

for combo in combinations(word, size):
    print(combo)
