# Create a Python function that accepts student name, roll number, course, and grade and returns a formatted string displaying these details.

# Write a pytest test file to verify that the function returns the correct formatted output for given sample input.

def student_details(name, rollNo , course , grade):
    result = (
        f"Student Name: {name}",
        f"Roll No: {rollNo}",
        f"Course: {course}",
        f"Grade: {grade}",
    )
    return result

if __name__ == "__main__":
    name = "Shrinivas"
    rollNo = 101
    course = "BCA",
    grade = "A+"
    print(student_details(name , rollNo , course, grade))
