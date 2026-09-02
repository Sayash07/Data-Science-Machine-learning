students = [
    {"name":"ashi", "gender": "male"},
    {"name":"Sayash ", "gender": "male"},
    {"name":"Nitan", "gender": "male"}
]

students_bool = all([el["gender"] == "male" for el in students])
print(students_bool)


