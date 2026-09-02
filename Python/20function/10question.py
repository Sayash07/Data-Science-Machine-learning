
# Q1: Find the average of three numbers using function.

def average(a,b,c):
    return ((a+b+c)/3)

result = average(a=1,b=2,c=3)
print(f"The average is {result}.")

# Q2:Find the palindrome of a number using function.
def is_palindrome(inp):
    if inp == inp[::-1]:
        return True
    else:
        return False

result = is_palindrome(inp = "Sayash")
print(result)


# Q3: Make a function for pronouns that takes one input(gender)

def pronouns(gender):
    if gender == "male":
        return "He"
    elif gender == "female":
        return "She"
    else:
        return "They"

result = pronouns(gender = "male")
print (result)

    


    