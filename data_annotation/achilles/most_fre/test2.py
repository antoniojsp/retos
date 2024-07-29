from collections import Counter

# Input strings
text = ['abc', 'def', 'abc', 'def', 'a', 'h', 'dfdfd', 'dfdfd', 'abc', 'dfdfd', 'dfdfd']

# Count occurrences of each string
string_counts = Counter(text)

# Get the 3 most frequent strings and their counts
most_frequent = string_counts.most_common(3)

# Print the results
for string, count in most_frequent:
    print(f"'{string}' appeared {count} times")
