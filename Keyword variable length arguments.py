def student(name,age,**marks):
    sum = 0
    print("Student's name is :",name)
    print("Student's age is:",age)
    print("Marks are :")
    for key,value in marks.items():
        print(key,":",value)
    for i in marks.values():
        sum+=i
    print("Total marks obtained :",sum)
    avg = sum/(len(marks))
    print("Average of the obtained marks is:",avg)
    print("----------------------------------------------")


student("Ram",25,English=90,Math = 98,Physics=99,Biology=92)
student("Chandu",26,English=31,Math = 30,Physics=35,Biology=96)
