from itertools import product

def combinations(string, size):
    chars = string.upper()
    print(f"Characters: {chars}")

    # Generate all combinations of given size with repetition
    all_combinations = [''.join(p) for p in product(chars, repeat=size)]
    print(f"All combinations: {all_combinations}")

    # Sort combinations
    sorted_combinations = sorted(all_combinations)
    print(f"Sorted combinations: {sorted_combinations}")

    unique = []
    duplicates = set()

    for comb in sorted_combinations:
        rev = comb[::-1]
        if rev in unique and rev != comb:  # avoid marking AA, BB as duplicate
            duplicates.add(comb)
        else:
            unique.append(comb)

    print(f"Unique combinations: {unique}")
    print(f"Duplicates (reverse matches): {list(duplicates)}")

    return unique


def main():
    chars = input("Enter the string: ").upper()
    num = int(input("Enter the size of combination: "))

    unique_combs = combinations(chars, num)

    print(f"\nAll possible combinations of '{chars}' of size {num} are:")
    print(", ".join(unique_combs))


if __name__ == "__main__":
    main()
