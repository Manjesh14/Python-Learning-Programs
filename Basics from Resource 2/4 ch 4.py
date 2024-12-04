#Dictionary
Biodata={
    "Name" : "Manjesh T S",
    "Age " : "18",
    "Student": True,
    "Subject":["English" , "Mathematics", "Physics"],
}
print(Biodata)
print(Biodata["Name"])

#Nested Dictionary
student={
    "Name_1": "Raju",
    "Marks":{
        "phy":97,
        "chem":96,
        "math":99,
    }
}
print(student["Marks"]["chem"])

#Dictionary Methods
print(tuple(Biodata.keys()))  #type casting
print(list(Biodata.keys()))   #type casting

print(len(list(Biodata.keys())))   #length

print(student.values())

print(list(student.items()))

# print(student["Name_2"])   #Error
print(student.get("Name_2"))   #no error

student.update({"city": "Kollegal"})
print(student)

#Sets in Python
Collections={1,2,3,3," Manjesh", "Kolle"," Kolle"}
print(Collections)
print(len(Collections))

Empty_set= set()
print(type(Empty_set))

Empty_set.add("Raaju")
Empty_set.add("Banglore")
Empty_set.remove("Banglore")
print(Empty_set)

Manjesh_collections={1,2, 14 ,18, "I "," Am"}
print(Manjesh_collections.pop())
print(Manjesh_collections.pop())