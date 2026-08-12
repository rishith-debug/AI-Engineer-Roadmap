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

Q8.What is the time complexity of checking membership in a Python set?

Answer:
Average-case O(1) because Python sets use a hash-table-based implementation.

That's an important one for your future DSA interviews, Rishith.

Q9.What is the purpose of the union() method in Python sets?

Answer:
union() combines the elements of two or more sets and returns a new set containing all unique elements from them.

Important: union() does not modify the original sets. It creates and returns a new set.

Q10.What does difference() return?

Answer:
It returns a new set containing the elements that are present in the first set but not present in the second set.

Q11: Is set difference symmetric?

Answer:
No. A.difference(B) and B.difference(A) can produce different results because the operation depends on the order of the sets.

Q12: What is symmetric difference between two sets?

Answer:
It returns the elements that are present in either of the two sets, but not in both.

Q13: Is symmetric_difference() affected by the order of the sets?

Answer:
No. Unlike difference(), symmetric difference is commutative:

A.symmetric_difference(B) gives the same result as B.symmetric_difference(A).

Q14. What is a subset?

Answer: A set A is a subset of B if every element of A is also present in B.

Q15. What is a superset?

Answer: A set A is a superset of B if A contains every element of B.

Q16. What do issubset() and issuperset() return?

Answer: They return a Boolean value: True or False.

Q17: What does isdisjoint() check?

Answer:
It checks whether two sets have no elements in common. It returns True if there are no common elements; otherwise, it returns False.

Q18: When would you use isdisjoint()?

Answer:
When you need to quickly check whether two collections have any common elements.

Q19: What is set comprehension?

Answer:
Set comprehension is a concise way to create a set using an expression, loop, and optionally a condition.

Q20: Why does set comprehension automatically remove duplicates?

Answer:
Because the result is a set, and sets store only unique elements.