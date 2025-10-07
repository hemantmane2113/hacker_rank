from itertools import product

def unique_combinations(string, size):
    chars = sorted(string.upper())  # sort for consistent order
    print(f"Characters: {chars}")

    seen = set()
    unique = []

    # Generate all combinations of given size with repetition
    for comb in product(chars, repeat=size):
        comb_str = ''.join(comb)
        rev = comb_str[::-1]

        # Only add if neither comb nor its reverse is seen
        if comb_str not in seen and rev not in seen:
            unique.append(comb_str)
            seen.add(comb_str)

    print(f"Unique combinations (ignoring reverse duplicates): {unique}")
    return unique


def main():
    chars = input("Enter the string: ").upper()
    size = int(input("Enter the size of combination: "))

    result = unique_combinations(chars, size)
    print(f"\nAll possible combinations of '{chars}' of size {size} are:")
    print(", ".join(result))


if __name__ == "__main__":
    main()
