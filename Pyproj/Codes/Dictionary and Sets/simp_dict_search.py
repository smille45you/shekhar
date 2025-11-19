students = {
    "riya": {"age": 21, "marks": 88},
    "rahul": {"age": 22, "marks": 76},
    "amit": {"age": 20, "marks": 92}
}

name = input("Enter student name: ").lower()

if name in students:
    print("Name :", name.capitalize())
    print("Age  :", students[name]["age"])
    print("Marks:", students[name]["marks"])
else:
    print("Student not found!")
