# DICTIONARIES

student = {
    "name": "Mabel",
    "age": 22,
    "courses": ["Math", "CompSci","Forensics"]

}

# Accessing and modifying
print(student["name"])   # "Mabel"
print(student.get("age"))   #22
student["age"] = 21   # Modifying value
student["email"] = "mabel@gmail.com"  # Adding new key-value pair


keys = student.keys()  # Get all keys
values = student.values()  # Get all values
items = student.items()  # Get all key-value pairs

print(keys) 
print(values)


  # Iterating through dictionaries
for key in student:
    print(f"{key}:{student[key]}")

for key, value in student.items():
    print(f"{key}:{value}")

# NESTED DICTIONARIES
company = {
    "employees":{
        "john": {"age": 30, "department": "HR"},
        "jane": {"age": 25, "department": "IT"}
    },
    "departments":["HR", "IT","FINANCE"]
}

print(company["employees"].items())
print(company["departments"])


#exercise

students_records = {
"student_001":{"name":"John",
               "age":"19",
               "major":"Computer Scince",
               "grades":[85,92,78]
},
"student_002":{"name":"Sarah",
                "age":"20",
                "major":"Biology",
                "grades":[90,88.95]
}}

students_records["student_003"] = {
    "name": "Mike",
    "age":  "18",
    "major": "Math",
    "grades": [82,79,91]
}
students_records["student_001"]["age"] = 20

for student_id, details in students_records.items():
    print(f"Student ID: {student_id},Name:{details['name']}, Major:{details['major']}")

