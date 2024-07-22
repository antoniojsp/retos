# my_list = [1, 2, 3, 4, 1, 2, 3, 4, 5]
#
# # Convert the list to a set to remove duplicates. Sets store unique elements.
# unique_list = set(my_list)
#
# # Convert the set back to a list if needed.
# deduplicated_list = list(unique_list)
#
# print(deduplicated_list)  # Output: [1, 2, 3, 4, 5]
my_list = [1, 2, 3, 4, 1, 2, 3, 4, 5]

seen = set()
deduplicated_list = [x for x in my_list if x not in seen and seen.add(x)]
print(seen)
print(deduplicated_list)  # Output: [1, 2, 3, 4, 5]

my_list = [1, 2, 3, 4, 1, 2, 3, 4, 5]

seen = set()
deduplicated_list = [x for x in my_list if not (x in seen or seen.add(x))]

print(deduplicated_list)  # Output: [1, 2, 3, 4, 5]