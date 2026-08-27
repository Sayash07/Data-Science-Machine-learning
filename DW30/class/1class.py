class Students: #first letter of class should be capital
    collage_name = "Deerwalk" # variables are called attributes in class
    address = "Kathmandu"

#get Student attribute
print(Students.collage_name)
print(Students.address)

# print(Student["collage_name"]) >> X (We cannot use this)
# change Student attribute
Students.collage_name = "Deerwalk Compare"
print(Students.collage_name)

#printing whole class
#print(Students) >> X (We cannot use this)