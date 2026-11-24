marks=['Sachin',50,55,67,76,89] 
# declares an list 'marks' to store marks of 'Sachin's
my_mark=[]
sum=0
# dynamic initialization
for number in range(5):
    newMark=int(input("Enter the marks:"))
    my_mark.append(newMark)

print("List elements are:")
for i in range(len(my_mark)):
    print("")

for i in range(len(my_mark)):
    sum+=my_mark[i]

