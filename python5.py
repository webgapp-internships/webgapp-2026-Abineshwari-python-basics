Students = ["Abi", "Hari","Madhu","Dinesh"]
Departments = ["CSE","ECE","IT","AIDS"]
Marks = (60, 70, 80, 90)

for i in range (len(Students)):
    print("Student name:",Students[i])
    print("Department  :",Departments[i])
    print("Marks       :",Marks[i])
    print("---------------------------")

def Rank(Marks):
    if (Marks[i] >= 35):
        return "Pass"
    else:
        return "Fail"

count = 0
i = 0
while i < len(Marks):
      if Marks[i] >= 35:
         count = i + 1
      i = i + 1
print("Number of pass",count)          

        

