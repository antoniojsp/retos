def num_of_substrings(string: str, n: int, m: int) -> int:
    """
    Counts substrings in a given string with the specified number of vowels and consonants.

    Args:
    - string: The input string.
    - n: Target number of vowels.
    - m: Target number of consonants.

    Returns:
    - Number of substrings that fulfill the criteria.
    """

    vowels = set('aeiou')
    count = 0

    # Iterate through all possible substrings
    for i in range(len(string)):  # Start index
        for j in range(i + 1, len(string) + 1):  # End index + 1
            sub_string = string[i:j]

            # Count vowels and consonants
            num_vowels = sum(1 for char in sub_string.lower() if char in vowels)
            num_consonants = len(sub_string) - num_vowels

            # If the substring matches the criteria, increment the count.
            if num_vowels == n and num_consonants == m:
                count += 1

    return count

# Example usage
result = num_of_substrings("ababbibbabh", 1, 3)
print(result)  # Output will be 5