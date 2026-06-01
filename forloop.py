marks = [36, 42, 53, 80, 50]

def check_result(mark):
    if mark >= 35:
        return "Pass"
    else:
        return "Fail"
    
for i in range(len(marks)):   

    result = check_result(marks[i])
    print("Student", i + 1,":", result)

        
    
