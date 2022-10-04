"""
Sum elements in the same index positions of lists.
"""

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6]
totals = []
if len(list1) > len(list2):
    for i in range(len(list2)):
        total = list1[i] + list2[i]
        totals.append(total)
    for i in range((len(list2) - len(list1)), 0):
        totals.append(list1[i])
    print(totals)
