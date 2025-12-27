from students import student_details

def test_student():
    expected = (
    "Student Name: Shrinivas",
    "Roll No: 101",
    "Course: BCA",
    "Grade: A+"
    )

    assert student_details("Shrinivas", 101,"BCA", "A+") == expected
