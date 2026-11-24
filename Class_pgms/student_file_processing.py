student_list=[]
with open("../student_details.txt","r",encoding="utf-8") as f:
    for line in f:
        total=sum([int (mark) for mark in line.strip().split()[3::]])
        rollno=line.strip().split()[0]
        firstname=line.strip().split()[1]
        secondname=line.strip().split()[2]
        name=firstname+ " " + secondname
        student_list.append(rollno + " "+ name + " "+ str(total) + "\n")


print(student_list)      
with open("output.txt","w",encoding="utf-8") as wp:
    wp.writelines(student_list)


