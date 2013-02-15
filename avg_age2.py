people = [ [ 'John', 42 ], [ 'James', 36 ], [ 'Sue', 38 ] ]

ages = []
for person in people:
    age = person[1]
    ages.append(age)

avg_age = sum(ages) / len(people)
print "Average age:", avg_age
