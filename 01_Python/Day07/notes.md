Q1. What is a list in Python?

Answer:
A list is an ordered, mutable collection that can store multiple values of different data types.

Q2. Why are lists called mutable?

Answer:
Because we can modify their elements after creation by adding, removing, or changing values.

Q3. Difference between List and Tuple?
List	Tuple
Mutable	Immutable
Uses []	Uses ()
Slower	Faster
Can be modified	Cannot be modified

Q4. Difference between append() and insert()?

append()

Adds an element at the end.

insert(index, value)

Adds an element at a specified index.

Q5. Difference between remove() and pop()?

remove(value)

Removes the specified value.

pop(index)

Removes an element by index.
Returns the removed element.

Q6. Difference between sort() and reverse()?

sort()

Arranges elements in ascending order by default.

reverse()

Reverses the current order of the list.
It does not sort the elements.
Q7. What does sort(reverse=True) do?

It sorts the list in descending order.

Q8. Difference between:
new_list = old_list

and

new_list = old_list.copy()

Assignment (=)

Both variables refer to the same list.
Changes in one affect the other.

copy()

Creates a separate independent list.
Changes do not affect the original list.

Q9. What does clear() do?

It removes all elements from the list, making it empty.

Example:

numbers.clear()

Output:

[]
Q10. What do max() and min() do?
max() returns the largest element.
min() returns the smallest element.