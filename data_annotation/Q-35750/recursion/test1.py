def get_ancestor(person, generations):
    if generations > 0:
        return get_ancestor(person.parent, generations - 1)
    # Missing a return for the base case!


person = Person("Alice", Person("Bob", Person("Charlie")))  # Example nested structure
ancestor = get_ancestor(person, 2)  # This will likely hit the recursion limit
