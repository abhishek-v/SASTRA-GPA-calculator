with open("gpa.txt","r") as file:
    total_credits=0
    total_grade=0
    grades={"S":10,"A+":9,"A":8,"B":7,"C":6,"D":5,"F":0,"E":0}
    grades_anna= {"S": 10, "A+": 9, "A": 9, "B": 8, "C": 7, "D":6,"F":0,"E":0}
    total_grade_anna=0
    grades_count={}
    for line in file:
        a=line.split("\t")
        grade_temp=a[5].replace("\n", "")
        grades_count[grade_temp]=grades_count.get(grade_temp,0)+1
        total_credits+=int(a[4])
        total_grade+=int(a[4])*grades[a[5].replace("\n","")]
        total_grade_anna+=int(a[4])*grades_anna[a[5].replace("\n","")]
    print("Total number of credits:",total_credits)
    print("Total number of grade points: ",total_grade)
    print("SASTRA GPA is: ",total_grade/total_credits)
    print("Anna University equivalent is :",total_grade_anna/total_credits)
    # a=total_grade+202
    # b=total_credits+28
    # print("final",a/b)
    #
    # a=a+150
    # b=b+21
    # print("final2",a/b)

    print("Grades count = ",grades_count)