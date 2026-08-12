SetA = {10, 20, 30}
SetB = {10, 20, 30, 40, 50}

Numbers = SetA.issubset(SetB)
print("the subset of SetA:",Numbers)
Numbers = SetB.issuperset(SetA)
print("the superset of SetB:",Numbers)
