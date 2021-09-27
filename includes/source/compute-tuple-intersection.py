def compute_intersection(tuple_one, tuple_two):
    """Return a tuple containing the elements in both input tuples."""
    result = ()
    for element in tuple_one:
        if element in tuple_two:
            result += (element,)
    return result


first_tuple = (1, "a", 2)
second_tuple = ("b", 2, "a")

intersection_tuple_one = compute_intersection(first_tuple, second_tuple)
intersection_tuple_two = compute_intersection(second_tuple, first_tuple)

print(intersection_tuple_one)
print(intersection_tuple_two)
