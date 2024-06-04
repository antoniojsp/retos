def first_non_repeating_character(stream):
  char_counts = {}  # Hash table
  ordered_chars = []  # Order of arrival

  for char in stream:
    char_counts[char] = char_counts.get(char, 0) + 1
    if char_counts[char] == 1:
      ordered_chars.append(char)

  for char in ordered_chars:
    if char_counts[char] == 1:
      return char

  return None  # No non-repeating characters found


print(first_non_repeating_character("aaaibbiiczzzllo"))