Q1. What does remove() do in a Python set?

Answer:
remove() deletes a specified element from a set.

If the element exists, it is removed successfully

Q2.What happens when remove() is used on an element that doesn't exist?

Answer:
It raises a KeyError because the specified element is not present in the set.

Q3. What is the difference between remove() and discard()?

remove()	discard()
Removes an element from a set	Removes an element from a set
Raises KeyError if element doesn't exist	Does not raise an error
Use when you expect the element to exist	Useful when the element may or may not exist

Q4. What does discard() do?
Answer: It removes a specified element from a set. If the element doesn't exist, it does nothing and doesn't raise an error.

Q5. Why use discard() instead of remove()?
Answer: Use discard() when you're not sure whether the element exists, because it won't raise a KeyError.

Q6. What does clear() do?
Answer: It removes all elements from a set and leaves an empty set.

Q7. Does clear() delete the set itself?
Answer: No. It removes the elements, but the set remains as an empty set.