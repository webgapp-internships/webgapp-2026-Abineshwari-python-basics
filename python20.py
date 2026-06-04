student=input("Enter the name:").split()
mark=[78,88,90,22]
department=("CSE","ECE","ECE","MECH")
def grade(mark):
    if mark>=35:
        return "pass"
    else:
        return "fail"
for i in range(len(student)):
    print("Name:",student[i])
    print("department:",department[i])
    print("mark:",mark[i])
    print("grade:",grade(mark[i]))
    print("________________________________")
count=0
i=0
while i<len(mark):
    if mark[i]>=35:
        count=i+1
    i=i+1
print("number of pass",count)