# with open("../student_details.txt","r+",encoding="utf-8") as file:
#        for line in file:
#               student_data=line.strip().split()
#               total=sum([int (x) for x in student_data[3::]])
#               file.write(" "+str(total))
                     
       

# with open('notes.txt', 'w+') as f:
#     f.write('Hello World')
#     content = f.read()
#     print(repr(content))

file=open("../student_details.txt","r",encoding="utf-8")
content=file.read()   
print(content)
print("-"*25)

file.seek(0)     #bring the file pointer to the begining of the file
content=file.readline()
print(content.strip())
content=file.readline()
print(content)
print("_"*30)
file.close()  # closses the file

file=open("../student_details.txt","a",encoding="utf-8")
file.write("\nAbcd")  #writting
file.close()




