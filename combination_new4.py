from itertools import product

def unique_combinations(string, size):
    chars = sorted(string.upper())
    print(f"Characters: {chars}")

    seen = set()
    unique = []

    for comb in product(chars, repeat=size):
        comb_str = ''.join(comb)
        rev = comb_str[::-1]

        # Always keep the lexicographically smaller of comb_str and rev
        chosen = min(comb_str, rev)

        if chosen not in seen:
            unique.append(chosen)
            seen.add(chosen)

    # Sort the final unique list for consistent output
    unique.sort()
    print(f"Unique combinations (choosing lexicographically smaller for reverse pairs): {unique}")
    return unique


def main():
    chars = input("Enter the string: ").upper()
    size = int(input("Enter the size of combination: "))

    result = unique_combinations(chars, size)
    print(f"\nAll possible combinations of '{chars}' of size {size} are:")
    print(", ".join(result))


if __name__ == "__main__":
    main()
