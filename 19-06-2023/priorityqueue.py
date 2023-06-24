student_grade=[]
student_grade.append((1,'akash'))
student_grade.append((4,'vinay'))
student_grade.sort(reverse=True)
print('yes')
print(student_grade)
student_grade.append((2,'eshwar'))
student_grade.sort(reverse= True)
student_grade.append((4,'sai'))
student_grade.sort(reverse=True)
print('priority wise sorted')
print(student_grade)
print('original queue')
while student_grade:
    print(student_grade.pop())
    
    