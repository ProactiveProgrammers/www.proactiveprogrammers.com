def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

values = [1, -2, 3.33]
print("values =", values)
apply_to_each(values, abs)
print("abs(values) =", values)
apply_to_each(values, int)
print("int(values) =", values)
apply_to_each(values, lambda x: x**2)
print("square(values) =", values)
