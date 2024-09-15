def num_of_substrings(string: str, n: int, m: int) -> int:
    vowels = set('aeiouAEIOU')
    count = 0

    for i in range(len(string)):
        vowel_count = 0
        consonant_count = 0

        for j in range(i, len(string)):
            if string[j] in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

            if vowel_count == n and consonant_count == m:
                count += 1

    return count

# Example usage
string = "ababbibbabh"
n = 1  # Number of vowels
m = 3  # Number of consonants
result = num_of_substrings(string, n, m)
print(result)  # Output: 5