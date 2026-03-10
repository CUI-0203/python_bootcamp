# SETS

fruits = {"apples", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}

# set operations
fruits.add("kiwi")   # add element
fruits.remove("banana")   # remove element
fruits.discard("pear")   # remove if exists(no error)

print(fruits)


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))   # {1,2,3,4,5,6,}
print(set1.intersection(set2))  # {3,4}
print(set1.difference(set2))  # {1,2}

#exercise

grades = [
("Taylor", "Science", 80),
("Justin","Maths",85),
("Katy","Maths",90),
("Gaga","Science",99),
("Selena","Physics",87),
("Adele","Maths",75)
]
students = set()
subjects = set()

for name, subject, grade in grades :
    students.add(name)
    subjects.add(subject)

print("students:", students)
print("subjects:", subjects)

