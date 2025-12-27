from students import student_details

def test_student():
    expected = (
        f"Student Name: Shrinivas\n",
        f"Roll No: 101\n",
        f"Course: BCA\n",
        f"Grade: A+"
    )
    assert student_details("Shrinivas", 101,"BCA", "A+") == expected