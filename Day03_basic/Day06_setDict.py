myResume = {
    "name": "Naresh Prasad Yadav",
    "course": "DevOps Engineering",
    "hobbies": "Singing",
    "address": "Haryana",
    "cgpa": 7
}

print(myResume)


myResume["company"] = "Google"

print(myResume)

print(len(myResume))

print("\nName and Hobbies:")
for key in ["name", "hobbies"]:
    print(key, ":", myResume[key])

del myResume["cgpa"]

print("\nFinal Dictionary:", myResume)