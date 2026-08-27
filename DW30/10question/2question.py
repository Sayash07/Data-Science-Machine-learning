students = [
    {"name": "Ram", "age": 20, "marks": 75},
    {"name": "Shyam", "age": 21, "marks": 85},
    {"name": "Hari", "age": 19, "marks": 65},
    {"name": "Sita", "age": 22, "marks": 90}
]

# make a list of name


ol = [el["name"] for el in students]
print(ol)


# find the student with highest marks

hs = sorted(students, key = lambda el:el["marks"], reverse=True)
print(hs[0])


#lowest marks

lowest_marks = sorted(students, key = lambda el:el["marks"])
print(lowest_marks[0])


# find the average of students:
average = [el["marks"] for el in students]
sum = 

print(average)

#find the student whose score is greater than 80
#find the 