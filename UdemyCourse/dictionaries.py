students = {"bob": 12, "rachel": 13, "emily":12}
print(students)

students["emily"] = 13
print(students)

del students["rachel"]
print(students)

students.update({"david": 13})
print(students)

print(len(students))