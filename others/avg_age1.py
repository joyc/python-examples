people = [ [ 'John', 42, 'pants' ], [ 'James', 36 ], [ 'Sue', 38 ] ]
    
total_age = 0
for person in people:
    age = person[1]
    total_age = total_age + age

avg_age = total_age / len(people)
print "Average age:", avg_age
